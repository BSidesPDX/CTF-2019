#!/usr/bin/env python2

FLAG = 'BSidesPDX{n1c3_j0b_y0u_f0und_t3h_m4g1c}'
SOURCE_FILE = 'magicnumbers_orig.c'
OUTPUT_FILE = 'magicnumbers.c'
X = 8
Y = 7

def encrypt_func(plaintxt):
    cipher = ''
    for i in range(len(plaintxt)):
        if i%2 == 0:
            v = ord(plaintxt[i]) + X
        else:
            v = ord(plaintxt[i]) - Y
        cipher += chr(v)
    return cipher

def generate_c_str(byte_str):
    result = ''
    for c in byte_str:
        v = ord(c)
        result += '\\x%02x' % v
    result = '"%s"' % result
    return result

def main():
    cipher = encrypt_func(FLAG)
    cipher_c_str = generate_c_str(cipher)

    with open(SOURCE_FILE, 'rb') as f:
        data = f.read()

    # Replace...
    data = data.replace('#define X 1', '#define X %d' % X)
    data = data.replace('#define Y 1', '#define Y %d' % Y)
    data = data.replace('#define FLAG_LENGTH 1', '#define FLAG_LENGTH %d' % len(cipher))
    data = data.replace('#define FLAG ""', '#define FLAG %s' % cipher_c_str)

    with open(OUTPUT_FILE, 'wb') as f:
        f.write(data)
    print('Flag written to source...')

main()
