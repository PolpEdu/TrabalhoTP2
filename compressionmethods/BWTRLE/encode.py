import sys
from itertools import groupby
import compressionmethods.BWT.BWTSRC as bw
import math as m


def rle_encode(input_string):
    return ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])


def bwt_rle(write, data, BLOCKSIZE):
    with open(write, "w") as f:
        f.close

    numero = m.ceil(len(data)/BLOCKSIZE)
    for i in range(numero):
        part_of_string = data[i*(BLOCKSIZE+1):((i+1)*(BLOCKSIZE+1))]

        if(part_of_string != ""):
            transform = bw.transform(part_of_string)
            new_data = rle_encode(transform)
            with open(write, "a+") as f:
                for n in new_data:
                    f.write(str(n))
        else:
            break
