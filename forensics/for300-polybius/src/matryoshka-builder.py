#!/usr/bin/env python2
import random
import zipfile
import os
import argparse

def encode_zip(input_data, additional_byte=None):
    if additional_byte == None:
        return encode_zip_no_byte(input_data)
    return encode_zip_additional_byte(input_data, additional_byte)

def encode_zip_additional_byte(input_data, password):
    pw = '0x%x' % ord(password)
    with open('data', 'wb') as f:
        f.write(input_data)
    with open(pw, 'wb'):
        pass
    zf = zipfile.ZipFile('temp.zip', mode='w', allowZip64=True)
    zf.write(pw)
    zf.write('data')
    zf.close()

    with open('temp.zip', 'rb') as f:
        data = f.read()

    # cleanup
    os.remove(pw)
    os.remove('temp.zip')
    os.remove('data')

    return data

def encode_zip_no_byte(input_data):
    with open('data', 'wb') as f:
        f.write(input_data)
    zf = zipfile.ZipFile('temp.zip', mode='w', allowZip64=True)
    zf.write('data')
    zf.close()

    with open('temp.zip', 'rb') as f:
        data = f.read()

    # cleanup
    os.remove('temp.zip')
    os.remove('data')

    return data

# (Friendlyname, function, accepts_singlebyte_bool)
FORMATS = [
    ('ZIP', encode_zip, True),
]

def get_rand_format(require_additional_byte_fmt):
    while True:
        i = random.randint(0,len(FORMATS)-1)

        # satisfy require_additional_byte_fmt
        if require_additional_byte_fmt:
            if FORMATS[i][2] != True:
                continue

        # requirements are good!
        return FORMATS[i]

def main(inner_fname, outter_fname, output_fname):
    with open(inner_fname, 'rb') as f:
        data = f.read()

    with open(outter_fname, 'rb') as f:
        outter_data = f.read()

    # the number of zip layers is equal to the number of bytes in outter_data
    layers = len(outter_data)
    print('Matryoshka zip will have %d layers' % layers)

    outter_counter = 0
    for i in range(layers):
        outter_chars_rem = len(outter_data) - outter_counter
        if outter_chars_rem == layers-i:
            require_additional_byte = True
        else:
            require_additional_byte = False

        fmt_str, fmt_func, additional_byte = get_rand_format(require_additional_byte)


        if additional_byte and outter_counter < len(outter_data):
            c = outter_data[len(outter_data)-1-outter_counter]
            outter_counter += 1
            data = fmt_func(data, c)
        else:
            data = fmt_func(data)

    with open(output_fname, 'wb') as f:
        f.write(data)
    print('done')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inner_input_fname", help="Filename to store at inner-most zip file")
    parser.add_argument("outter_input_fname", help="Filename to store at byte-by-byte as empty filename")
    parser.add_argument("output_fname", help="Filename to write the final matryoshka zip to")
    args = parser.parse_args()

    main(args.inner_input_fname, args.outter_input_fname, args.output_fname)
