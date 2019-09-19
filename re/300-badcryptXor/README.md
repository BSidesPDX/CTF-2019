# RE 300 - Bad CryptXor

## Description

You're presented with an x86-64 Linux binary as well as an encrypted file.  The program used to encrypt the file is a pretty simple XOR cipher, however, the file is hidden behind a password-protected, custom cryptor.  So the user will have to unwind the cryptor or use a debugger to reveal the embedded 2nd binary.

Give player binary and encrypted file from `distFiles`

## Deployment

1. Run `./builder.py`

## Challenge

Can you help us decrypt this file?  It appears to have been encrypted using the attached program, but the program is password-protected and it appears to be obfuscated.

flag: `BSidesPDX{tH1s^B4d^b0Y^C4n^f1t^s0^m4NY^x0rs^iN^IT!}`
