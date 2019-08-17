# RE 100 - Magic Numbers

## Description

You're presented with an x86-64 Linux binary.  The binary will notify the user that there are 3 magic numbers they must find.  These numbers are static, hardcoded values.  After each number is entered, the binary will either tell the user that the number is incorrect or prompt for the next number.  Once all 3 numbers are correctly entered, the program will "decrypt" and print out the flag.

Give player binary from `distFiles`

## Deployment

1. Change flag in `flag_injector.py`
2. Run `make`

## Challenge

Can you find the hard-coded, magic numbers?  If you've never reverse-engineered a binary before, now is the perfect time to try!  [It's Dangerous to go Alone! Take This](https://ghidra-sre.org/).

flag: `BSidesPDX{n1c3_j0b_y0u_f0und_t3h_m4g1c}`
