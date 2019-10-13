# PWN 300 - pwnchess

## Description

You're presented with an x86-64 Linux binary and a copy of libc.so running on the remote server.  The binary is compiled with all default anti-exploit mitigations except for PIE.  The binary allows the you to peform one of three operations; read one byte at an arbitrary, write one byte to an arbitrary location, or exit.  The catch is that you are allowed to perform only 2 operations.  So first you must write a larger value to the global variable, moves, memory address.  Next, you will have to leak the libc address by performing multiple reads to an address from the GOT section.  Once a libc address is leaked, offsets can be calculated using the provided version of libc.  Then, you use the free leak the application gives to the stack to calculate the address on the stack where the return address is read from.  You can finally write a ret2libc ROP chain to this location, and finally either exhaust all remaining moves or write 0 to the moves address to trigger the ROP chain.

## Deployment

If anything needs to be done to deploy it

## Challenge

I made a game, I call it pwnchess.  You can read/write any memory address, but can you pop a shell in so few moves?  Only the most elitest of hackers will be able to get checkmate.

pwnchess.bsidespdxctf.party:31337

NOTE: Flag file is at `/app/flag.txt`

Flag: `BSidesPDX{th3_0nlYY_w1nn1ng___m0v_1s__2_g3t_y0urs3lf_m0re_m0v3s_aka_ch34t_2_w1n!!}`
