# HollowDex Vault — Writeup

**Challenge:** Android credential checker. Enter the right 32-character hex key and it grants access.
**Answer:** `c19e6e4be6148b5581809ae7291c9cfe`

---

## Overview

The APK looks straightforward: `MainActivity` reads input, calls `Verifier.verifyFlag()`, and
shows `ACCESS GRANTED` / `ACCESS DENIED`. The twist ("Except it isn't") is that the body of
`verifyFlag` is **hollowed out** — its bytecode is stored XOR-encrypted inside `classes.dex`, and
the native library `libhollowdex.so` decrypts it in memory at runtime.

### Files in the APK

| File | Size | Purpose |
|------|------|---------|
| `classes.dex` | 3828 | DEX with the app logic (hollowed `verifyFlag`) |
| `lib/arm64-v8a/libhollowdex.so` | 5632 | Native loader that decrypts the method at runtime |
| `AndroidManifest.xml` | 1568 | App manifest (`com.hollowdex`) |
| `res/layout*/activity_main.xml` | — | UI layouts |
| `resources.arsc` | 1240 | Compiled resources |

---

## Step 1 — Reconnaissance

### Command Executed

```bash
file hollowdex.apk
jadx hollowdex.apk
unzip -l hollowdex.apk
unzip -o hollowdex.apk -d extracted/
xxd classes.dex
strings -a classes.dex
strings -a lib/arm64-v8a/libhollowdex.so
readelf -a lib/arm64-v8a/libhollowdex.so
```

### What `strings` revealed

**`classes.dex`** contains the class/method names and UI strings:

```
Lcom/hollowdex/Verifier;
verifyFlag
ACCESS DENIED
ACCESS GRANTED
hollowdex
```

**`libhollowdex.so`** contains the smoking gun — a native routine that reads the process memory:

```
JNI_OnLoad
/proc/self/maps
com/hollowdex/Verifier
(Ljava/lang/String;)Z
/proc/self/mem
r-xp
r--p
.apk
verifyFlag
fopen  fgets  strstr  sscanf  fclose
open   lseek  write  close
```

This tells us the library:
1. Locates `com.hollowdex.Verifier` and its static method `verifyFlag(String)Z`.
2. Parses `/proc/self/maps` to find a mapped region containing `.apk` whose start begins with the
   `dex\n` magic.
3. Opens `/proc/self/mem` and writes data back into that mapped DEX — i.e. it **patches the method
   code at runtime**.

---

## Step 2 — Reverse the native library

The `.so` is AArch64. There is no `jadx`-style tool for native code, so I disassembled it with
**Capstone** (`pip install capstone`) and a small Python script.

```python
from capstone import *
data = open('lib/arm64-v8a/libhollowdex.so','rb').read()
code = data[0x8a0:0x8a0+0x33c]
md = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
for insn in md.disasm(code, 0x18a0):
    print(f"{insn.address:08x}: {insn.mnemonic}\t{insn.op_str}")
```

### Resolving the imports

I mapped each PLT stub to its symbol using `.rela.plt` (readelf output). The `.plt` stubs start at
`0x1be0`, and each 16-byte stub loads from a GOT slot:

| PLT stub | GOT slot | Symbol |
|----------|----------|--------|
| `0x1c00` | `0x2eb0` | `__cxa_finalize` |
| `0x1c10` | `0x2eb8` | `__cxa_atexit` |
| `0x1c20` | `0x2ec0` | `__register_atfork` |
| `0x1c30` | `0x2ec8` | `fopen` |
| `0x1c40` | `0x2ed0` | `fgets` |
| `0x1c50` | `0x2ed8` | `strstr` |
| `0x1c60` | `0x2ee0` | `sscanf` |
| `0x1c70` | `0x2ee8` | `fclose` |
| `0x1c80` | `0x2ef0` | `operator new[]` (`_Znam`) |
| `0x1c90` | `0x2ef8` | `open` |
| `0x1ca0` | `0x2f00` | `lseek` |
| `0x1cb0` | `0x2f08` | `write` |
| `0x1cc0` | `0x2f10` | `close` |
| `0x1cd0` | `0x2f18` | `operator delete[]` (`_ZdaPv`) |

### Decompiled `JNI_OnLoad` (reconstructed)

```c
jint JNI_OnLoad(JavaVM* vm, void* reserved) {
    JNIEnv* env;
    if (vm->GetEnv(&env, JNI_VERSION_1_6) != 0) return JNI_ERR;

    jclass cls = env->FindClass("com/hollowdex/Verifier");
    if (!cls) return JNI_ERR;

    jmethodID m = env->GetStaticMethodID(cls, "verifyFlag", "(Ljava/lang/String;)Z");
    if (!m) return JNI_ERR;

    uint32_t code_off = *(uint32_t*)((char*)m + 8);   // dex_code_item_offset_

    FILE* fp = fopen("/proc/self/maps", "r");
    char line[512];
    uintptr_t dex_base = 0;

    while (fgets(line, sizeof line, fp)) {
        if (!strstr(line, ".apk")) continue;
        if (!strstr(line, "r--p") && !strstr(line, "r-xp")) continue;
        uintptr_t start, end;
        if (sscanf(line, "%lx-%lx", &start, &end) != 2) continue;
        if (*(uint32_t*)start == 0x0A786564) {   // "dex\n"
            dex_base = start;
            break;
        }
    }
    fclose(fp);
    if (!dex_base || !code_off) return JNI_VERSION_1_6;

    code_item* code = (code_item*)(dex_base + code_off);
    size_t n = code->insns_size * 2;             // bytes
    char* buf = new char[n];

    for (size_t i = 0; i < n; i++)
        buf[i] = code->insns[i] ^ key[i & 15];    // 16-byte key

    int fd = open("/proc/self/mem", O_RDWR);
    lseek(fd, (off_t)code->insns, SEEK_SET);
    write(fd, buf, n);
    close(fd);
    delete[] buf;
    return JNI_VERSION_1_6;
}
```

The `+8` offset into `ArtMethod` is the `dex_code_item_offset_` field, which points at the method's
`code_item` inside the DEX.

---

## Step 3 — Extract the XOR key

The key is a 16-byte constant in `.rodata` (loaded with `ldr q0, [x10, #0x700]`):

```
.rodata @ 0x700:
59 0e 7a 65 14 c3 be a1 e3 c1 e7 81 e3 c1 ef 01
```

Other `.rodata` strings (offsets) used by the loader:

| Offset | String |
|--------|--------|
| `0x700` | XOR key (16 bytes) |
| `0x710` | `/proc/self/maps` |
| `0x720` | `com/hollowdex/Verifier` |
| `0x737` | `r-xp` |
| `0x73c` | `%lx-%lx` |
| `0x744` | `(Ljava/lang/String;)Z` |
| `0x75a` | `/proc/self/mem` |
| `0x769` | `r--p` |
| `0x76e` | `r` |
| `0x770` | `.apk` |
| `0x775` | `verifyFlag` |

---

## Step 4 — Parse the DEX and decrypt the method

I wrote a small DEX parser in Python to walk the header, string/type/method IDs and class_data, and
found `Verifier.verifyFlag`:

```
class[5] = Lcom/hollowdex/Verifier
  method "verifyFlag"  access=0x1  code_off=0x62c
```

`code_item` at `0x62c`:

```
registers_size = 0x0f  (15)
ins_size       = 0x02
outs_size      = 0x02
tries_size     = 0x00
debug_info_off = 0x7d9
insns_size     = 0x9c  (156 code units = 312 bytes)
insns          @ 0x63c
```

Decrypt:

```python
import struct
data = bytearray(open('classes.dex','rb').read())
key = bytes.fromhex('590e7a6514c3bea1e3c1e781e3c1ef01')
insns_off = 0x63c
for i in range(156*2):
    data[insns_off + i] ^= key[i & 15]
open('classes_patched.dex','wb').write(bytes(data))
```

---

## Step 5 — Decompile the real method

I downloaded **baksmali** and **jadx**:

```bash
curl -sSL -o baksmali.jar https://bitbucket.org/JesusFreke/smali/downloads/baksmali-2.5.2.jar
curl -sSL -o jadx.zip https://github.com/skylot/jadx/releases/download/v1.5.1/jadx-1.5.1.zip

java -jar baksmali.jar d classes_patched.dex -o smali_out/
```

The decrypted `verifyFlag` (smali → pseudocode):

```java
boolean verifyFlag(String input) {
    if (input == null || input.length() != 32) return false;

    byte[] b = new byte[16];
    for (int i = 0; i < 16; i++) {
        int hi = Character.digit(input.charAt(2*i),   16);
        int lo = Character.digit(input.charAt(2*i+1), 16);
        if (hi < 0 || lo < 0) return false;
        b[i] = (byte)((hi << 4) | lo);
    }

    // a = first 8 bytes, b_ = last 8 bytes (both big-endian u64)
    long a = 0, bb = 0;
    for (int i = 0; i < 8; i++) a  = (a  << 8) | (b[i]   & 0xff);
    for (int i = 0; i < 8; i++) bb = (bb << 8) | (b[i+8] & 0xff);

    long x  = C0 ^ a ^ ROL(bb + C0, 17);
    long b1 = bb ^ ROL(x + C1, 17) ^ C1;
    long y  = x  ^ ROL(b1 + C2, 17) ^ C2;

    return b1 == C3 && y == C4;
}
```

### Constants (from the `const-wide` instructions in smali)

```
C0 = 0x243f6a8885a308d3
C1 = 0x13198a2e03707344
C2 = 0xa4093822299f31d0
C3 = 0x554d47c35cf8ea95
C4 = 0xb4bc6cae39400b7a
```

(`C0`/`C1`/`C2` are the first six Blowfish P-array entries packed into three 64-bit words.)

`ROL(x, 17)` is a rotate-left by 17:

```python
def rol(x, n):
    return ((x << n) | (x >> (64 - n))) & 0xFFFFFFFFFFFFFFFF
```

---

## Step 6 — Invert and solve

Both final conditions use known targets (`b1 == C3`, `y == C4`), so the system is directly
invertible:

```python
C0 = 0x243f6a8885a308d3
C1 = 0x13198a2e03707344
C2 = 0xa4093822299f31d0
C3 = 0x554d47c35cf8ea95
C4 = 0xb4bc6cae39400b7a

def rol(x, n):
    return ((x << n) | (x >> (64 - n))) & 0xFFFFFFFFFFFFFFFF

x = C4 ^ rol((C3 + C2) & 0xFFFFFFFFFFFFFFFF, 17) ^ C2
x &= 0xFFFFFFFFFFFFFFFF
b = C3 ^ rol((x + C1) & 0xFFFFFFFFFFFFFFFF, 17) ^ C1
b &= 0xFFFFFFFFFFFFFFFF
a = C0 ^ x ^ rol((b + C0) & 0xFFFFFFFFFFFFFFFF, 17)
a &= 0xFFFFFFFFFFFFFFFF

flag = f"{a:016x}{b:016x}"
print(flag)
```

### Results

```
x = 0xef7e59bc2814c806
b = 0x81809ae7291c9cfe
a = 0xc19e6e4be6148b55

flag = c19e6e4be6148b5581809ae7291c9cfe
```

### Verification (forward pass)

```
b1 == C3  -> True
y  == C4  -> True
```

---

## Final answer

```
c19e6e4be6148b5581809ae7291c9cfe
```

I took `c19e6e4be6148b5581809ae7291c9cfe` and put it in cyberchef and from hex. It gave me an output with random bytes. I put it to sha256 anyways because why not.
It gave me this output: `7295614c872c071d88fe8b29b5af155fd44f837b5d986f5d74a2524de883241b`

So I got the flag: `CTF{7295614c872c071d88fe8b29b5af155fd44f837b5d986f5d74a2524de883241b}`