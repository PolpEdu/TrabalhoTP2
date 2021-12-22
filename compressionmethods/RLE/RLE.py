from struct import *
from re import sub
import time


def writetofileENC(file, encoding):
    output_file = open("./encoded/"+file.split(".")[0] + ".rle", "wb")
    for x in encoding:
        output_file.write(pack('>B', ord(x)))

    output_file.close()


def readfromfile(f):
    file = open(f, "rb")
    rle = ""
    # Reading the compressed file.
    while True:
        rec = file.read(1)  # only 1 byte, B standard size is 1
        if len(rec) != 1:
            break
        (data, ) = unpack('>B', rec)  # unpack with >B
        rle += chr(data)
    file.close()
    return rle


def writetofileDEC(file, decode):
    # storing the decompressed string into a file.
    output_file = open(file, "wb")
    output_file.write(bytearray(decode.encode()))

    output_file.close()
    return len(decode)


def compressRLE(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding


def decompressRLE(s):
    decoded = ""
    number = ""
    for x in range(0, len(s)):
        if s[x].isdigit():
            number += str(s[x])
            continue
        else:
            if number == "" or type(number) == "str":
                continue
            number = int(number)
            decoded += s[x] * number
            number = ""
    return decoded
