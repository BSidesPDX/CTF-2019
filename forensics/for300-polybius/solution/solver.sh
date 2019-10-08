#!/bin/bash

# apt install mtd-utils, https://integriography.wordpress.com/2015/03/16/mounting-a-jffs2-dd-image-in-linux/ (Googling "mounting jffs2 file system")
jffs2dump -b -c -r -e jffs2.little.bin $1 >/dev/null

# Use binwalk to extract the contents of the jffs2 filesystem
binwalk -e jffs2.little.bin >/dev/null

# Move grandmother.zip to current directory and cleanup binwalk output
mv _jffs2.little.bin.extracted/jffs2-root/fs_1/grandmother.zip grandmother.zip && rm -rf _jffs2.little.bin.extracted

# Extract the Matryoshka zip
python2 matryoshka-extractor.py grandmother.zip flag.gpg polybius.jpg

# Get the password from the strings of the polybius iamge
PASSWORD=$(strings polybius.jpg | grep Password | cut -d' ' -f2)

# Decrypt the gpg file using the password
gpg -o flag.txt --batch --passphrase $PASSWORD flag.gpg

# Clean up the intermediate files
rm polybius.jpg grandmother.zip jffs2.little.bin flag.gpg