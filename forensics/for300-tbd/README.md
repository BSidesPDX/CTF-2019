# Forensics 300 - [Name]

## Description

This challenge involves learning about the jff2 file format, writing a script to process a matryoshka zip file and unveil a hidden message in the file names, and then finding a string that doesn't belong.

## Deployment

This file can be served from object storage and doesn't require any interactive components. In order to recreate the file to be deployed, you will need `python2`, `gpg`, and `mkfs.jffs2` which can be obtained via `apt install mtd-utils`. Once you have these installed, follow these instructions:

1. `mkdir tmp && cp src/* tmp/`
1. `cat gpg-password.txt >> polybius.jpg`
1. `PASSWORD=$(cat gpg-password.txt | grep Password | cut -d' ' -f2)`
1. `gpg --batch --passphrase $PASSWORD -o flag.gpg -c flag.txt`
1. `python2 matryoshka-builder.py polybius.jpg flag.gpg grandmother.zip`
1. `mkdir jffs2`
1. `mv grandmother.zip jff2s/`
1. `mkfs.jffs2 -d jffs2 -o jffs2.bin -b`

The output file, `jffs2.bin` will be a big-endian jffs2 filesystem and the `file` command on most modern systems will only detect it as data. `jffs2.bin` should be uploaded to object storage, with a download link provided at the end of the challenge text.

## Challenge

I have recently taken up an interest in arcade games. While I was digging around in Joe Fitz's basement, I stumbled across a strange cabinet that I'd never seen before. But across the top it said "Polybius" and that name sounded familiar. Unfortunately, I wasn't able to boot up the machine to play it, but using the skills I learned from all of Joe's training, I was able to dump the firmware for the machine, but it's in a file format I don't know. Can you help? [Download The Firmware](https://example.com)


Flag: `BSidesPDX{P01yb1u$_1$_r341_bu7_th3r3_4r3_14y3r$_t0_7h3_c0n$p1r4cy}`