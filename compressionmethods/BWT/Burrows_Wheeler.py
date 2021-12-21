
import os
from struct import *
import compressionmethods.BWT.BWTSRC as bw
import math as m


def encode(data, blocksize):
    numero = m.ceil(len(data)/blocksize)
    final_string = ""
    for i in range(numero):
        part_of_string = data[i*(blocksize+1):((i+1)*(blocksize+1))]

        if(part_of_string != ""):
            transform = bw.transform(part_of_string)
            final_string += transform
        else:
            break

    return final_string


def writetofileENC(fich, final_string):
    with open(fich, "wb") as f:
        for i in range(0, len(final_string)):
            f.write(pack('>B', ord(final_string[i])))
        f.close()
    return len(final_string)


def readfileENC(fich):
    file = open("./encoded/"+fich.split(".")[0]+".bwt", "rb")
    bwt = ""
    # Reading the compressed file.
    while True:
        rec = file.read(1)  # only 1 byte, B standard size is 1
        if len(rec) != 1:
            break
        (data, ) = unpack('>B', rec)  # unpack with >B
        bwt += chr(data)
    file.close()
    return bwt


def decode(bwt, blocksize):

    final_string = ""
    blocksize += 2
    numero = m.ceil(len(bwt)/blocksize)

    for i in range(numero):
        part_of_string = bwt[i*(blocksize+1):((i+1)*(blocksize+1))]

        if part_of_string != "":
            inversed = bw.inverse(part_of_string)
            final_string += inversed

    return final_string


def writetofileDEC(fich, final_string):
    # storing the decompressed string into a file.
    output_file = open(fich, "w")
    output_file.write(final_string)

    output_file.close()
