TARGET=magicnumbers

CC=gcc
CFLAGS =-g

all:
	@/usr/bin/env python2 flag_injector.py
	gcc -o $(TARGET) $(TARGET).c

clean:
	@rm -f $(TARGET)
	@rm -f magicnumbers.c
