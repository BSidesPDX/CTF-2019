# PWN 100 - rot13

## Description

You're presented with an x86 Linux binary.  The binary is compiled with NX, PIE, and stack canaries all disabled.  You are prompted for input, then the program performs a ROT13 on the input, and finally prints back the result.  There is a buffer overflow on the input, as more bytes are read than the allocated buffer size.  The problem is, the input is modified by the program (each byte is incremented by 13), so the payload must be modified in the reverse (each byte subtracted by 13) before sending it to the program.  The actual payload is simple, as it can just be shellcode with a gadget to jump to it.

## Deployment

Change the flag file at `src/flag.txt` and run `make` in `src/`.

## Challenge

I wrote a simple program that performs a rot13 on your input.

rot13.bsidespdxctf.party:1337

NOTE: Flag file is at `/app/flag.txt`

Flag: `BSidesPDX{pwn_it__l1k3_its_1999_AAAAAAAAAAAAAAAAAAAAAAAAAAAA%}`
