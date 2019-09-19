#!/usr/bin/env python2
import os
import subprocess

def stage2cryptor(payload):
	KEY = 0x42

	enc = ''

	for c in payload:
		enc += chr(ord(c) ^ KEY)

	pretty = ''
	for c in enc:
		pretty += '0x%02x, ' % ord(c)

	return pretty


def stage3cryptor(fname):
	with open(fname, 'rb') as f:
		payload = f.read()

	enc = ''

	i = 0
	prev = 0x41
	key = 77
	for c in payload:
		m = (i%128)
		ckey = m^key
		cval = ord(c) ^ ckey
		enc += chr(cval)
		i+=1

	pretty = ''
	for c in enc:
		pretty += '0x%02x, ' % ord(c)
	return pretty

# read stage1.asm
with open('stage1.asm', 'rb') as f:
	stage1_asm = f.read()

# compile final
os.system('gcc final.c -o final')
os.system('strip final')

# xor encrypt final
enc_final = stage3cryptor('final')

# Compile stage2
os.system('nasm -f elf64 stage2.asm && ld -o stage2 stage2.o')
os.system('strip stage2')
ret = subprocess.check_output(['bash', './getstage2bytes.sh'])
stage2_bytes = eval('"%s"' % ret)

# xor encrypt stage2
stage2_str = stage2cryptor(stage2_bytes)

# inject stage2 cipher into stage1
stage1_asm = stage1_asm.replace('stage2: db 0x00', 'stage2: db ' + stage2_str)

# inject final cipher into stage1.asm
stage1_asm = stage1_asm.replace('stage3: db 0x00', 'stage3: db ' + enc_final)

# Write new asm file
with open('stage1_gen.asm', 'wb') as f:
	f.write(stage1_asm)

# compile stage1
os.system('nasm stage1_gen.asm -f elf64 -o stage1_gen.o')
os.system('gcc -no-pie stage1_gen.o -o challenge')
os.system('strip challenge')
