push rbp
mov rbp, rsp
sub rsp, 0x8

mov rax, fs:0xffffffffffffffe8
mov [rbp-0x8], rax
mov rdi, 1
lea rsi, [rbp-0x8]
mov rdx, 0x4
mov rax, 0x1
syscall

mov rax, fs:0xffffffffffffffec
mov [rbp-0x8], rax
mov rdi, 1
lea rsi, [rbp-0x8]
mov rdx, 0x4
mov rax, 0x1
syscall

mov rax, fs:0xfffffffffffffff0
mov [rbp-0x8], rax
mov rdi, 1
lea rsi, [rbp-0x8]
mov rdx, 0x4
mov rax, 0x1
syscall

mov rax, fs:0xfffffffffffffff4
mov [rbp-0x8], rax
mov rdi, 1
lea rsi, [rbp-0x8]
mov rdx, 0x4
mov rax, 0x1
syscall

mov rax, fs:0xfffffffffffffff8
mov [rbp-0x8], rax
mov rdi, 1
lea rsi, [rbp-0x8]
mov rdx, 0x4
mov rax, 0x1
syscall

mov rax, fs:0xfffffffffffffffc
mov [rbp-0x8], rax
mov rdi, 1
lea rsi, [rbp-0x8]
mov rdx, 0x4
mov rax, 0x1
syscall

leave
ret