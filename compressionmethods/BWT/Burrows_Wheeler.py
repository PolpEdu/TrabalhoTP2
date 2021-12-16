# Apply burrows Wheeler Encoding
# def BWTencode(filename, data):
import os
from struct import *
def encode(fich, data, blocksize):
    with open("./encoded/"+fich.split(".")[0]+".bwt", "wb") as f:
        for i in range(0, len(data), blocksize):  # divisão em Blocos
            bwttry = bwt_tranf(data[i-blocksize:i])
            for n in bwttry:
                f.write(pack('>H',int(ord(n))))
        f.close
        

    #return os.stat(fich).st_size/os.stat("./encoded/"+fich.split(".")[0]+".bwt").st_size,


def bwt_tranf(d):
    Input = d
    assert "£" not in Input                     # Input string cannot contain £
    Input = Input + "£"                         # Add "£" to the end of the string
    table = [Input[i:] + Input[:i]
             for i in range(len(Input))]  # Table of rotations of string

    table = sorted(table)

    last_column = [row[-1:]
                   for row in table]             # Last characters of each row
    bwt = ''.join(last_column)
    return bwt


def decode(fich):
    file = open("./encoded/"+fich.split(".")[0]+".bwt", "rb")
    compressed_data = []
    # Reading the compressed file.
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data, ) = unpack('>H', rec)
        compressed_data.append(data)

    file.close()


    bwt = compressed_data

    table = [""] * len(bwt)  # Make empty table

    for _ in range(len(bwt)):
        table = [bwt[i] + table[i] for i in range(len(bwt))]  # Add a column of r
        print('unsorted = ', table)
        table = sorted(table)
        print('sorted    =', table)

        inverse_bwt = [row for row in table if row.endswith("£")][0]  # Find the correct row (ending in £)

        # Get rid of start and end markers
        inverse_bwt = inverse_bwt.rstrip("£")

        with open("./decoded/decodedBWT"+fich, "wb") as f:
            f.write(bytearray(inverse_bwt.encode()))
            f.close()





'''
    to_encode = "".join(last_column)
    output_file = open("./encoded/"+filename.split(".")[0]+".bwt", "wb")
    # escrever em binario não como "w" texto, se for como texto deve escrever alguns metadados indesejados
    output_file.write(bytearray(to_encode.encode()))
    output_file.close()
'''

'''
    output_file = open("./decoded/decodedBWT"+filename, "wb")
    # escrever em binario não como "w" texto, se for como texto deve escrever alguns metadados indesejados
    output_file.write(bytearray(stringfinal.encode()))
    output_file.close()
'''
