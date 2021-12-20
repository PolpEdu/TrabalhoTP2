from __future__ import print_function
from string import ascii_letters
from struct import *
import sys


def writetofile(name, sequence):
    output_file = open(name, "wb")
    for data in sequence:

        # B para ser 1 bytes, não vou usar int (>H) para não gastar espaço desnecessário
        print(data)
        if data > 255:
            print("Error: data > 255")
            sys.exit(1)

        output_file.write(pack('>B', data))

    output_file.close()
    return len(sequence)


def move2front_encode(strng, symboltable):
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad

    return sequence


def readfile(name):
    input_file = open("./encoded/"+name.split(".")[0] + ".mtf", "rb")
    sequence = []
    while True:
        data = input_file.read(1)
        if not data:
            break
        sequence.append(unpack('>B', data)[0])
    return sequence


def outputfile(name):
    output_file = open(name, "wb")
    # escrever em binario não como "w" texto, se for como texto deve escrever alguns metadados indesejados
    output_file.write(bytearray(decoded.encode()))
    output_file.close()


def move2front_decode(sequence, symboltable):

    chars, pad = [], symboltable[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad

    decoded = "".join(chars)

    return decoded


if __name__ == '__main__':
    SYMBOLTABLE = list(ascii_letters)
    for s in ['broood', 'bananaaa', 'hiphophiphop']:
        encode = move2front_encode(s, SYMBOLTABLE)
        print('%14r encodes to %r' % (s, encode), end=', ')
        decode = move2front_decode(encode, SYMBOLTABLE)
        print('which decodes back to %r' % decode)
        assert s == decode, 'Whoops!'
