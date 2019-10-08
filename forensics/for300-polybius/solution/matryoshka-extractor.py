#!/usr/bin/env python2
import zipfile
import os
import shutil
import argparse

def zip_walk(fname_in):
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')

    zipfname = './tmp/data.zip'
    shutil.copyfile(fname_in, zipfname)

    outer_data = ''
    while True:
        # check if zipfile
        if not zipfile.is_zipfile(zipfname):
            with open(zipfname, 'rb') as f:
                inner_data = f.read()

            shutil.rmtree('./tmp')
            return (outer_data, inner_data)

        with zipfile.ZipFile(zipfname, 'r') as zip_file:
            data_found = False
            for name in zip_file.namelist():
                if name[:2] == '0x':
                    outer_data += chr(eval(name))
                elif name == 'data':
                    data_found = True

            if data_found:
                zip_file.extract('data', './tmp/')
            else:
                raise Exception('data file not found!')

        # move data -> data.zip
        os.rename('./tmp/data', zipfname)

def main(fname_in, outer_out_fname, inner_out_fname):
    outer_data, inner_data = zip_walk(fname_in)

    with open(outer_out_fname, 'wb') as f:
        f.write(outer_data)
    with open(inner_out_fname, 'wb') as f:
        f.write(inner_data)
    print('Done!')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("matryoshka_fname", help="Matryoshka Zip Filename")
    parser.add_argument("outer_output_fname", help="Filename to write 'outer' file contents")
    parser.add_argument("inner_output_fname", help="Filename to write 'inner' file contents")
    args = parser.parse_args()

    main(args.matryoshka_fname, args.outer_output_fname, args.inner_output_fname)
