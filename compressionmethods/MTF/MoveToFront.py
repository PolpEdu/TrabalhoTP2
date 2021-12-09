from __future__ import print_function
from string import ascii_letters
from struct import *

 
def move2front_encode(name,strng, symboltable):
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad


    output_file = open("./encoded/"+name.split(".")[0] + ".mtf", "wb")
    for data in sequence:
        output_file.write(pack('>H',int(data)))
        
    output_file.close()

    return sequence
 
def move2front_decode(name,symboltable):
    input_file = open("./encoded/"+name.split(".")[0] + ".mtf", "rb")
    sequence = []
    while True:
        data = input_file.read(2)
        if not data: break
        sequence.append(unpack('>H',data)[0])

    chars, pad = [], symboltable[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    
    to_encode ="".join(chars)

    output_file = open("./decoded/decodedMTF"+name, "wb")
    #escrever em binario não como "w" texto, se for como texto deve escrever alguns metadados indesejados
    output_file.write(bytearray(to_encode.encode())) 
    output_file.close()
    
    return ''.join(chars)
 
if __name__ == '__main__':
    SYMBOLTABLE = list(ascii_letters)
    for s in ['broood', 'bananaaa', 'hiphophiphop']:
        encode = move2front_encode(s, SYMBOLTABLE)
        print('%14r encodes to %r' % (s, encode), end=', ')
        decode = move2front_decode(encode, SYMBOLTABLE)
        print('which decodes back to %r' % decode)
        assert s == decode, 'Whoops!'