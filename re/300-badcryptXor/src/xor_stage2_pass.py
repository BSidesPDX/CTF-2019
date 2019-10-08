#!/usr/bin/env python2

password = 'I_c4n_x0r!'

enc = ''
for c in password:
	enc += chr(ord(c) ^ 0x1)

print(enc)

hexs = ''
for c in enc:
	hexs += '0x%x ' % ord(c)

print(hexs)
