#!/bin/bash

# Make a working directory
mkdir tmp/

cp polybius.jpg tmp/

# Cat the password file to the end of the image
cat gpg-password.txt >> tmp/polybius.jpg

# Grab the password from the password file
PASSWORD=$(cat gpg-password.txt | grep Password | cut -d' ' -f2)

# GPG encrypt the flag using the password
gpg --batch --passphrase $PASSWORD -o tmp/flag.gpg -c flag.txt

# Build the matryoshka zip file
python2 matryoshka-builder.py tmp/polybius.jpg tmp/flag.gpg tmp/grandmother.zip

# Make a directory that will serve as the root of the jffs2 filesystem
mkdir tmp/jffs2; mv tmp/grandmother.zip tmp/jffs2/grandmother.zip

# Move the matryoshka zip to the jffs2 folder
#mv tmp/grandmother.zip tmp/jff2s/

# Make the jffs2 filesystem using directory jffs2, output to jffs2.bin, -b for big endian
mkfs.jffs2 -d tmp/jffs2 -o jffs2.bin -b

# Cleanup working directory
rm -rf tmp/
