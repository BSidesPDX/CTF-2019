extern asprintf
extern execl

section .text
    global main

main:
    push rbp

    ; anti-debug
    ; TODO

    ; anti-debug passed!
    mov     rax, 1
    mov     rdi, 1
    mov     rsi, message
    mov     rdx, length
    syscall

    mov     rax, 0

loop:
    cmp     rax, stage2_len
    je loader1
    mov     dil, [stage2+rax]
    xor     dil, 0x42
    mov     [stage2+rax], dil
    inc rax
    jmp loop

loader1:
    push loader2
    push correct_pw
    push correct_pw_len
    push incorrect_pw
    push incorrect_pw_len
    push stage3
    push stage3_len
    jmp stage2

loader2:
    ; memfd
    mov rax, 319
    mov rdi, null_byte
    mov rsi, 1
    syscall

    ; save fd
    mov r15, rax

    ; write
    mov rax, 1
    mov rdi, r15
    mov rsi, stage3
    mov rdx, stage3_len
    syscall

    ; asprintf
    mov rdi, rsp
    mov rsi, proc_fmt
    mov rdx, r15
    mov eax, 0x0
    call asprintf

    ; exec
    mov r8d, 0x0
    mov rcx, null_byte
    mov rdx, null_byte
    mov rsi, null_byte
    mov rdi, [rsp]
    mov eax, 0x0
    call execl

    jmp exit

exit:
    mov rax, 60
    mov rdi, 0
    syscall

section .data
    null_byte: db 0,0
    proc_fmt: db "/proc/self/fd/%i",0

    message: db 'Enter the password',0x0a
    length: equ $-message

    correct_pw: db 'password is correct!',0x0a
    correct_pw_len: equ $-correct_pw

    incorrect_pw: db 'wrong password...',0x0a
    incorrect_pw_len: equ $-incorrect_pw

    stage2: db 0x00
    stage2_len: equ $-stage2

    stage3: db 0x00
    stage3_len: equ $-stage3
