# RATatouille — Writeup

**Challenge:** A Rust "telemetry implant" stays dormant in VMs but prepared a secret "signature dish" on real hardware. Flag: `DCTF{<64 lowercase hex>}`.

## Recon

- `file`: stripped 64-bit PIE ELF, Rust (paths `src/main.rs`, `src/browser.rs`).
- `readelf -S`: unusual custom section **`.recipe`** — 70 bytes (`0x47b1b6`), exactly `5 + 64 + 1` = the flag length.
- `strings`: `RATATOUILLE_STATION`, `/proc/meminfo`, `/proc/cpuinfo`, DMI paths, VM/anti-debug markers (`QEMU`, `vbox`, `TracerPid`), and Ratatouille movie terms (`remy`, `gusteau`, `auguste`, `confit`).

## Key insight

The "calibration" check (`0x125f0`) verifies a menu struct contains fixed strings and returns a bitmask compared to `0x1ff`. The recipe decryptor (`0x1d6c0`) feeds those **same 7 strings** into an FNV-1a hash to derive the decryption seed — so the key is **deterministic**, not machine-dependent.

## Decryption

1. `seed = fnv1a64(linux, x86_64, remy, gusteau, /bin/bash, auguste-gusteau, confit-byaldi)`
   - between each: `h ^= 0xff; h *= 0x100000001b3`; final `h ^= 0x72617461746f7569`
   - (the 7th string has a trailing `\n` trimmed before hashing)
2. XOR the `.recipe` bytes with a wyrand-style stream:
   - `mix(x) = x ^ x>>12 ^ x<<25 ^ x>>27`
   - keystream byte = `(mix(state) * 0x2545f4914f6cdd1d) >> 56`

```python
MASK = (1<<64)-1
PRIME = 0x100000001b3

def fnv(strings):
    h = 0xcbf29ce484222325
    for s in strings:
        for b in s:
            h ^= b; h = (h*PRIME) & MASK
        h ^= 0xff; h = (h*PRIME) & MASK
    return (h ^ 0x72617461746f7569) & MASK

def mix(x):
    x = (x ^ (x>>12)) & MASK
    x = (x ^ (x<<25)) & MASK
    x = (x ^ (x>>27)) & MASK
    return x

recipe = bytes.fromhex("565cbcc4fd91c4b61c1a2114a9dc9955"
    "1276bdd5a28f7941788f2c0bf05486cf"
    "fd6e898624cec530c477371cf1d63452"
    "5ef2a2e44ae84a6a73a607f0bde64d0b834442aafd64")

seed = fnv([b"linux", b"x86_64", b"remy", b"gusteau",
            b"/bin/bash", b"auguste-gusteau", b"confit-byaldi"])

out = bytearray(70)
C = 0x2545f4914f6cdd1d
for i in range(0, 70, 2):
    h = mix(seed)
    out[i]   = recipe[i]   ^ (((h*C) & MASK) >> 56)
    seed = mix(h)
    out[i+1] = recipe[i+1] ^ (((seed*C) & MASK) >> 56)

print(bytes(out).decode())
```

## Flag

```
DCTF{e132475cf5b732c2ba714f028a159d957ace5f790edb629b99387621d03bbc61}
```

The result matches the implant's own validator (`DCTF{` + 64 hex + `}`), confirming the seed is correct.
