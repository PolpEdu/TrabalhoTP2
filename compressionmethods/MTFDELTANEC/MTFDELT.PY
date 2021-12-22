import compressionmethods.MTF.MoveToFront as mtf
from itertools import starmap, islice
from operator import sub
from struct import *
import math


def decode(enc, alf):
    enc = delta_dec(enc)
    decoded = mtf.move2front_decode(enc, alf)
    return decoded


def delta_dec(l):
    new_l = [l[0]]
    for x in range(1, len(l)):
        new_l.append(l[x] + new_l[x - 1])
    return new_l


def delta_enc(l):
    return [l[0], *starmap(sub, zip(islice(l, 1, None), l))]


def encode(data, alf):
    mtfencoded = mtf.move2front_encode(data, alf)
    encoded = delta_enc(mtfencoded)
    # print(encoded)
    return encoded


def writeoriginal(fi, data):
    mtf.writetofileDEC(fi, data)
    return len(data)


def writetofile(fi, data):
    with open(fi, "wb") as f:
        for i in range(0, len(data)):
            # print(data[i])
            # print(type(data[i]))
            f.write(pack('>b', data[i]))
        f.close()


def readfile(f):
    file = open(f, "rb")
    enc = []
    # Reading the compressed file.
    while True:
        rec = file.read(1)  # only 1 byte, b standard size is 1
        if len(rec) != 1:
            break
        (data, ) = unpack('>b', rec)  # unpack with >h
        enc.append(data)
    file.close()
    return enc
