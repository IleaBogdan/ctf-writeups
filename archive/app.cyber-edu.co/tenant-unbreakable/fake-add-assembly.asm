section .data
    msg db 'Results:', 10
    msg_len equ $ - msg
    
    fmt db 'var_%02X = %d (0x%X)', 10
    fmt_len equ $ - fmt

section .bss
    ; Reserve space for variables
    var_FC resd 1
    var_F8 resd 1
    var_F4 resd 1
    var_F0 resd 1
    var_EC resd 1
    var_E8 resd 1
    var_E4 resd 1
    var_E0 resd 1
    var_DC resd 1
    var_D8 resd 1
    var_D4 resd 1
    var_D0 resd 1
    var_CC resd 1
    var_C8 resd 1
    var_C4 resd 1
    var_C0 resd 1
    var_BC resd 1
    var_B8 resd 1
    var_B4 resd 1
    var_B0 resd 1
    var_AC resd 1
    var_A8 resd 1
    var_A4 resd 1
    var_A0 resd 1
    var_9C resd 1
    var_98 resd 1
    var_94 resd 1
    var_90 resd 1
    var_8C resd 1
    var_88 resd 1
    var_84 resd 1
    var_80 resd 1
    var_7C resd 1
    var_78 resd 1
    var_74 resd 1
    var_70 resd 1
    var_6C resd 1
    var_68 resd 1
    var_64 resd 1
    var_60 resd 1
    var_5C resd 1
    var_58 resd 1
    var_54 resd 1
    var_50 resd 1
    var_4C resd 1
    var_48 resd 1
    var_44 resd 1
    var_40 resd 1
    var_3C resd 1
    var_38 resd 1
    var_34 resd 1
    var_30 resd 1
    var_2C resd 1
    var_28 resd 1
    var_24 resd 1
    var_20 resd 1
    var_1C resd 1
    var_18 resd 1
    var_14 resd 1
    var_10 resd 1
    var_C resd 1
    var_8 resd 1
    var_4 resd 1

section .text
    global _start
    extern printf

_start:
    ; Initialize variables
    mov dword [var_FC], 0x3C
    mov dword [var_F8], 0x7
    mov dword [var_F4], 0x2A
    mov dword [var_F0], 0x2A
    mov dword [var_EC], 0x20
    mov dword [var_E8], 0x26
    mov dword [var_E4], 0x78
    mov dword [var_E0], 0x3
    mov dword [var_DC], 0x5A
    mov dword [var_D8], 0x1A
    mov dword [var_D4], 0x68
    mov dword [var_D0], 0x0
    mov dword [var_CC], 0x27
    mov dword [var_C8], 0xA
    mov dword [var_C4], 0x64
    mov dword [var_C0], 0xF
    mov dword [var_BC], 0x4B
    mov dword [var_B8], 0x14
    mov dword [var_B4], 0x5F
    mov dword [var_B0], 0xA
    mov dword [var_AC], 0x64
    mov dword [var_A8], 0xF
    mov dword [var_A4], 0x55
    mov dword [var_A0], 0xA
    mov dword [var_9C], 0x55
    mov dword [var_98], 0x15
    mov dword [var_94], 0x55
    mov dword [var_90], 0x20
    mov dword [var_8C], 0x34
    mov dword [var_88], 0x1
    mov dword [var_84], 0x2A
    mov dword [var_80], 0x2A
    mov dword [var_7C], 0x35
    mov dword [var_78], 0x2A
    mov dword [var_74], 0x21
    mov dword [var_70], 0x20
    mov dword [var_6C], 0x21
    mov dword [var_68], 0x23
    mov dword [var_64], 0x21
    mov dword [var_60], 0x23
    mov dword [var_5C], 0x64
    mov dword [var_58], 0x19
    
    ; Perform all additions
    mov edx, [var_FC]
    mov eax, [var_F8]
    add eax, edx
    mov [var_54], eax
    
    mov edx, [var_F4]
    mov eax, [var_F0]
    add eax, edx
    mov [var_50], eax
    
    mov edx, [var_EC]
    mov eax, [var_E8]
    add eax, edx
    mov [var_4C], eax
    
    mov edx, [var_E4]
    mov eax, [var_E0]
    add eax, edx
    mov [var_48], eax
    
    mov edx, [var_DC]
    mov eax, [var_D8]
    add eax, edx
    mov [var_44], eax
    
    mov edx, [var_D4]
    mov eax, [var_D0]
    add eax, edx
    mov [var_40], eax
    
    mov edx, [var_CC]
    mov eax, [var_C8]
    add eax, edx
    mov [var_3C], eax
    
    mov edx, [var_C4]
    mov eax, [var_C0]
    add eax, edx
    mov [var_38], eax
    
    mov edx, [var_BC]
    mov eax, [var_B8]
    add eax, edx
    mov [var_34], eax
    
    mov edx, [var_B4]
    mov eax, [var_B0]
    add eax, edx
    mov [var_30], eax
    
    mov edx, [var_AC]
    mov eax, [var_A8]
    add eax, edx
    mov [var_2C], eax
    
    mov edx, [var_A4]
    mov eax, [var_A0]
    add eax, edx
    mov [var_28], eax
    
    mov edx, [var_9C]
    mov eax, [var_98]
    add eax, edx
    mov [var_24], eax
    
    mov edx, [var_94]
    mov eax, [var_90]
    add eax, edx
    mov [var_20], eax
    
    mov edx, [var_8C]
    mov eax, [var_88]
    add eax, edx
    mov [var_1C], eax
    
    mov edx, [var_84]
    mov eax, [var_80]
    add eax, edx
    mov [var_18], eax
    
    mov edx, [var_7C]
    mov eax, [var_78]
    add eax, edx
    mov [var_14], eax
    
    mov edx, [var_74]
    mov eax, [var_70]
    add eax, edx
    mov [var_10], eax
    
    mov edx, [var_6C]
    mov eax, [var_68]
    add eax, edx
    mov [var_C], eax
    
    mov edx, [var_64]
    mov eax, [var_60]
    add eax, edx
    mov [var_8], eax
    
    mov edx, [var_5C]
    mov eax, [var_58]
    add eax, edx
    mov [var_4], eax
    
    ; Print all results
    push dword [var_54]
    push dword [var_54]
    push dword 0x54
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_50]
    push dword [var_50]
    push dword 0x50
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_4C]
    push dword [var_4C]
    push dword 0x4C
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_48]
    push dword [var_48]
    push dword 0x48
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_44]
    push dword [var_44]
    push dword 0x44
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_40]
    push dword [var_40]
    push dword 0x40
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_3C]
    push dword [var_3C]
    push dword 0x3C
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_38]
    push dword [var_38]
    push dword 0x38
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_34]
    push dword [var_34]
    push dword 0x34
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_30]
    push dword [var_30]
    push dword 0x30
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_2C]
    push dword [var_2C]
    push dword 0x2C
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_28]
    push dword [var_28]
    push dword 0x28
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_24]
    push dword [var_24]
    push dword 0x24
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_20]
    push dword [var_20]
    push dword 0x20
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_1C]
    push dword [var_1C]
    push dword 0x1C
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_18]
    push dword [var_18]
    push dword 0x18
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_14]
    push dword [var_14]
    push dword 0x14
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_10]
    push dword [var_10]
    push dword 0x10
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_C]
    push dword [var_C]
    push dword 0x0C
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_8]
    push dword [var_8]
    push dword 0x08
    push fmt
    call printf
    add rsp, 16
    
    push dword [var_4]
    push dword [var_4]
    push dword 0x04
    push fmt
    call printf
    add rsp, 16
    
    ; Exit program
    mov eax, 60
    xor edi, edi
    syscall