
import os
from struct import *
import compressionmethods.BWT.BWTSRC as bw
import math as m


def encode(fich, data, blocksize):
    numero = m.ceil(len(data)/blocksize)
    final_string = ""
    for i in range(numero):
        part_of_string = data[i*(blocksize+1):((i+1)*(blocksize+1))]

        if(part_of_string != ""):
            transform = bw.transform(part_of_string)
            final_string += transform
        else:
            break

    with open("./encoded/"+fich.split(".")[0]+".bwt", "wb") as f:
        for i in range(0, len(final_string)):
            f.write(pack('>B', ord(final_string[i])))
        f.close()

    return len(final_string)


def decode(fich, blocksize):
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

    final_string = ""
    blocksize += 2
    numero = m.ceil(len(bwt)/blocksize)

    for i in range(numero):
        part_of_string = bwt[i*(blocksize+1):((i+1)*(blocksize+1))]

        if part_of_string != "":
            inversed = bw.inverse(part_of_string)
            final_string += inversed
        else:
            break

    with open("./decoded/decodedBWT"+fich, "wb") as f:
        f.write(bytearray(final_string.encode()))
        f.close()

    return len(final_string)
