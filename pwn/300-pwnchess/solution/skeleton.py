#!/usr/bin/env python2
from pwn import *

# You might have to change this depending on the architecture of the binary
context.arch = 'amd64'

# Toggle these variables to turn debugging or remote exploitation on/off
REMOTE = False
DEBUG = False

# Update these to match your environment
FNAME = '../distFiles/pwnchess'
HOST = '127.0.0.1'
PORT = '31337'

elf = ELF(FNAME)
if REMOTE:
    libc = ELF('../distFiles/libc-2.27.so')
else:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

def getp():
    if REMOTE:
        p = remote(HOST, PORT)
    elif DEBUG:
        p = process(['gdbserver', 'localhost:1234', FNAME])
    else:
        p = process([FNAME])
    return p

p = getp()
p.interactive()
