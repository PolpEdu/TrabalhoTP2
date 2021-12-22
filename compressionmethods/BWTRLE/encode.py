import sys
from itertools import groupby
import compressionmethods.BWT.Burrows_Wheeler as BWT

import math as m


def rle_encode(input_string):
    return ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])


def bwt_rle(write, data, BLOCKSIZE):

    encoded_BWT = BWT.encode(data, BLOCKSIZE)
    encoded_RLE = rle_encode(encoded_BWT)

    with open(write, "w") as f:
        f.write(encoded_RLE)
        f.close()
