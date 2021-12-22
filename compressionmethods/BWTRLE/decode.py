from re import sub
import compressionmethods.BWT.BWTSRC as BWTSRC
import math as m


def writetofile(write, data):
    with open(write, "w") as f:
        f.write(data)
        f.close()


def decode(fname, BLOCKSIZE):
    file = open(fname, "r")
    texto = file.readlines()
    data = ''.join(texto)
    totalstring = ""

    numero = m.ceil(len(data)/BLOCKSIZE)
    for i in range(numero):
        part_of_string = data[i*(BLOCKSIZE+1):((i+1)*(BLOCKSIZE+1))]

        stringtoinvert = rle_decode(part_of_string)
        new_data = BWTSRC.inverse(stringtoinvert)
        totalstring += str(new_data)

    return totalstring


def rle_decode(s):
    decoded = ""
    number = ""
    for x in range(0, len(s)):
        if s[x].isdigit():
            number += str(s[x])
            continue
        else:
            if number == "":
                continue
            number = int(number)
            decoded += s[x] * number
            number = ""
    return decoded


if __name__ == "__main__":
    rle_decode("1£36 22.1,1:7.1,9.3,1t7d1h1d1f1o1g1d1y2D1d1D2d1f18d1t2,3e8,1d3e1t1p1f1y1e3h1d1e1t1l1h1,1h1,1e1,3e2m1f1r1d1s1:1,5:5,1;6,1e4,1:1;1,6:3,1;1:1d1;2,1s6,1y4,1s1n1,1;1h1,6g1,1:8,1d2e1m1l1m1n2e1b1e1d1y1:2d1e1,3d1e1d1s2h1s1h1e1s4d1,1e1t3d1e2d1e3g3t1y1d1e1d2e1h1e1h2e1h1e2h1d1t1d1h1r1e2o1t2d31e1d6e1o1r1o1n1u2d1r2d1o1w")
