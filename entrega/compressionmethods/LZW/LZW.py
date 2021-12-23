# LZW Encoder / Decoder
# Name: Aditya Gupta
# ID: 800966229
# ITCS 6114

from struct import *

from numpy import byte


def writetofile(compressed_data, name):
    # storing the compressed string into a file (byte-wise).
    output_file = open("./encoded/"+name.split(".")[0] + ".lzw", "wb")
    for data in compressed_data:  # DA stora a um elemento da data
        # cada elemento de um indice do dicionário é little endian ">" e ocupa 2 bytes "H" (ver documentação do pack() ), por isso a MAX_WIDTH NÃO PODE SER MAIOR QUE 16 bits
        output_file.write(pack('>H', int(data)))

    output_file.close()


def compress(data, code_width):
    maximum_table_size = pow(2, int(code_width))

    # Building and initializing the dictionary.
    dictionary_size = 256  # no maximo o dicionario tem 256 elemtnos
    dictionary = {chr(i): i for i in range(dictionary_size)}
    string = ""             # String is null.
    compressed_data = []    # variable to store the compressed data.

    # iterating through the input symbols.
    # LZW Compression algorithm
    for symbol in data:
        string_plus_symbol = string + symbol  # get input symbol.
        if string_plus_symbol in dictionary:
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            if(len(dictionary) <= maximum_table_size):
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
            string = symbol

    if string in dictionary:
        compressed_data.append(dictionary[string])

    return compressed_data


def readfromfile(input_file):
    compressed_data = []
    file = open("./encoded/"+input_file.split(".")[0]+".lzw", "rb")

    # Reading the compressed file.
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data, ) = unpack('>H', rec)
        compressed_data.append(data)

    file.close()

    return compressed_data


def decompress(compressed_data):
    next_code = 256
    decompressed_data = ""
    string = ""

    # Building and initializing the dictionary.
    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

    # iterating through the codes.
    # LZW Decompression algorithm
    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + (string[0])
        decompressed_data += dictionary[code]
        if not(len(string) == 0):
            dictionary[next_code] = string + (dictionary[code][0])
            next_code += 1
        string = dictionary[code]

    decompressedstr = "".join(decompressed_data)

    return decompressedstr


def writeoutputDECtofile(input_file, strdecompressed):
    # storing the decompressed string into a file.
    output_file = open(input_file, "wb")
    output_file.write(bytearray(strdecompressed.encode()))

    output_file.close()
