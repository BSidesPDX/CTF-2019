mov rbp, rsp
add rsp, 1000
mov rax, 0 		; read
mov rdi, 0 		; stdin
mov rsi, rsp	; dest
mov rdx, 11		; length
syscall

; check if we got expected length back
cmp rax, 11
jne exit

; Check password (I_c4n_x0r!)
mov rax, 0
mov dl, [rsp+rax]
xor dl, 1
cmp dl, 0x48
jne exit

inc rax
mov dl, [rsp+rax]
xor dl, 1
cmp dl, 0x5e
jne exit

inc rax
mov dl, [rsp+rax]
xor dl, 1
cmp dl, 0x62
jne exit

inc rax
mov dl, [rsp+rax]
xor dl, 1
cmp dl, 0x35
jne exit

inc rax
mov dl, [rsp+rax]
xor dl, 1
cmp dl, 0x6f
jne exit

inc rax
mov dl, [rsp+rax]
xor dl, 1
cmp dl, 0x5e
jne exit

inc rax
mov dl, [rsp+rax]
xor dl, 1
cmp dl, 0x79
jne exit

inc rax
mov dl, [rsp+rax]
xor dl, 1
cmp dl, 0x31
jne exit

inc rax
mov dl, [rsp+rax]
xor dl, 1
cmp dl, 0x73
jne exit

inc rax
mov dl, [rsp+rax]
xor dl, 1
cmp dl, 0x20
jne exit

success:
	mov rsp, rbp
	pop r8 ; stage3 length
	pop r9 ; stage3 buff
	pop rax ; errormsg
	pop rax ; errormsg

	; write correct pw to stdout
	mov rax, 1 		; write
	mov rdi, 1 		; stdout

	pop rdx ; length
	pop rsi	; buf
	syscall

	jmp decrypt

loop:
	jmp loop

decrypt:
	pop r15 ; return
	mov r10, 0 ; counter

decloop:
	cmp r10, r8
	je decfinish

	mov rax, r10
	mov edx, 0
	mov ebx, 128
	div ebx

	; edx == counter % 128
	;edx+40 is our key
	xor edx, 77
	mov al, [r9+r10]
	xor al, dl
	mov [r9+r10], al

	inc r10
	jmp decloop

decfinish:
	jmp r15

exit:
	mov rsp, rbp
	pop rax
	pop rax

	mov rax, 1 		; write
	mov rdi, 1 		; stdout
	pop rdx ; length
	pop rsi ; buf
	syscall
	mov rax, 60
	mov rdi, 0
	syscall
