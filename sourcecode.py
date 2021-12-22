
import os
from DataInfo import *
import time
import sys

import compressionmethods.MTF.MoveToFront as MTF
import compressionmethods.LZW.LZW as LZW
import compressionmethods.HuffmanCODEC.huffmancodec as hf
import compressionmethods.BWT.Burrows_Wheeler as BWT
import compressionmethods.LZWHUFFMAN.lzwhuffman as LZWHUF
import compressionmethods.MTFHUFF.MTFHUFFMAN as MTFHUFF
import compressionmethods.BZIP2.BZIP2 as BZIP2
import compressionmethods.MTFDELTANEC.MTFDELT as MTFDE

FILES = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]


def main():
    # escrever os dados num arquivo byte-wise
    for file in FILES:

        print("Nome: "+file)
        data, alfabeto = DataInfo.readfiledata(file)

        tamanhooriginal = os.stat(
            './dataset/'+file).st_size

        print("Tamanho data: "+str(tamanhooriginal) +
              " bytes, tamanho alfabeto: "+str(len(alfabeto)))

        ocorrencias = DataInfo.get_ocorrencias(data, alfabeto)
        # criarhist(ocorrencias, alfabeto)

        print(
            f"No pior dos casos codificavamos {file} com: {DataInfo.bitssimbolo(len(alfabeto)):.5f} bits/simbolo")

        # limite mínimo teórico para o número médio de bits por símbolo NORMAL
        print(
            f"Entropia de {file}: {DataInfo.entropia(ocorrencias):.5f} bits/simbolo")

        #
        #
        #
        #
        # HUFFMAN CODEC - COMPRIMIR PAR AUM FICHEIRO (A BIT STREAM DATA) e depois ver quanto é q ele ocupa.
        start = time.time()
        [symbols, lenght] = hf.Huffman_encode(data, file)
        symbols = symbols[1:]  # remove EOF
        end = time.time()
        print(f"HUFFMAN encode: {end-start:.5f}s")
        hf.Huffman_decode(file)
        end = time.time()
        print(f"HUFFMAN decode: {end-start:.5f} segundos")

        tablesize = os.stat(
            './encoded/'+file.split(".")[0]+'.huffTable').st_size

        huffdata = os.stat('./encoded/'+file.split(".")[0]+'.huffData').st_size

        compressedfilesize = tablesize+huffdata

        compressionrate = calcrate(tamanhooriginal, compressedfilesize)

        filesize = os.stat('./decoded/decodedHuffman'+file).st_size

        DataInfo.printinfo(tamanhooriginal, filesize,
                           compressedfilesize, compressionrate)

        checkfiles("./decoded/decodedHuffman"+file, "./dataset/"+file)

        #
        #
        #
        # 8 BITS - DATA SET COM 2^8 ENTRADAS
        # MAX_WIDTH não pode ser maior que 16 porque 2*8 = 16 bits
        # LZW CODEC
        MAX_WIDTH = 15  # para termos o maior nr de blocos
        start = time.time()
        compressed_data = LZW.compress(data, MAX_WIDTH)
        LZW.writetofile(compressed_data, file)
        end = time.time()
        print(f"LZW encode: {end-start:.5f} segundos")

        readcompressed_LZW_data = LZW.readfromfile(file)
        decoded = LZW.decompress(readcompressed_LZW_data)
        LZW.writeoutputDECtofile("./decoded/decodedLZW"+file, decoded)
        end = time.time()
        print(f"LZW decode: {end-start:.5f} segundos")

        compressedfilesize = os.stat(
            './encoded/'+file.split(".")[0]+'.lzw').st_size

        filesize = os.stat('./decoded/decodedLZW'+file).st_size

        compressionrate = calcrate(tamanhooriginal, compressedfilesize)
        DataInfo.printinfo(tamanhooriginal, filesize,
                           compressedfilesize, compressionrate)

        checkfiles("./decoded/decodedLZW"+file, "./dataset/"+file)

        #
        #
        #
        #
        # MTF+DELTA
        start = time.time()
        compressed = MTFDE.encode(data, alfabeto)
        MTFDE.writetofile(
            "./compressionmethods/MTFDELTANEC/"+file.split(".")[0] + ".mtfdelta", compressed)
        end = time.time()
        print(f"MTF+DELTA encode: {end-start:.5f} segundos")

        readfromfile = MTFDE.readfile(
            "./compressionmethods/MTFDELTANEC/"+file.split(".")[0] + ".mtfdelta")
        mtfdecoded = MTFDE.decode(readfromfile, alfabeto)
        filesize = MTFDE.writeoriginal(
            "./compressionmethods/MTFDELTANEC/decodedMTFDELTANEC"+file, mtfdecoded)
        end = time.time()
        print(f"MTF+DELTA decode: {end-start:.5f} segundos")

        compressedfilesize = os.stat(
            "./compressionmethods/MTFDELTANEC/"+file.split(".")[0] + ".mtfdelta").st_size

        compressionrate = calcrate(tamanhooriginal, compressedfilesize)
        DataInfo.printinfo(tamanhooriginal, filesize,
                           compressedfilesize, compressionrate)

        checkfiles(
            "./compressionmethods/MTFDELTANEC/decodedMTFDELTANEC"+file, "./dataset/"+file)
        '''
        BLOCKSIZE = 100
        start = time.time()
        encoded_BWT = BWT.encode(data, BLOCKSIZE)
        compressedfilesize = BWT.writetofileENC(
            "./encoded/"+file.split(".")[0]+".bwt", encoded_BWT)
        end = time.time()
        print(f"BWT encode: {end-start:.5f} segundos")

        decoded_BWT = BWT.decode(encoded_BWT, BLOCKSIZE)
        filesize = BWT.writetofileDEC(
            "./decoded/decodedBWT"+file, decoded_BWT)
        end = time.time()
        print(f"BWT decode: {end-start:.5f} segundos")

        compressionrate = calcrate(tamanhooriginal, compressedfilesize)
        DataInfo.printinfo(tamanhooriginal, filesize,
                           compressedfilesize, compressionrate)

        checkfiles("./decoded/decodedBWT"+file, "./dataset/"+file)
        '''
        #
        #
        #
        #
        #
        # lzw+huffman

        MAX_WIDTH = 12  # para termos mais blocos o que beneficia a compressão de huffman
        start = time.time()
        LZWHUF.lzwHuffmanenc(file, data, MAX_WIDTH)
        end = time.time()
        print(f"ENCODE LZW+HUFFMAN: {end-start:.5f} segundos")
        LZWHUF.lzwHuffmandec(file)
        end = time.time()
        print(f"DECODE: LZW+HUFFMAN: {end-start:.5f} segundos")
        compressedfilesize = os.stat(
            "./compressionmethods/LZWHUFFMAN/" +
            file.split(".")[0]+".LZWhuffData").st_size+os.stat(
            "./compressionmethods/LZWHUFFMAN/" +
            file.split(".")[0]+".LZWhuffTable").st_size

        filesize = os.stat(
            "./compressionmethods/LZWHUFFMAN/decodedLZWHUFFMAN"+file).st_size

        compressionrate = calcrate(tamanhooriginal, compressedfilesize)
        DataInfo.printinfo(tamanhooriginal, filesize,
                           compressedfilesize, compressionrate)

        checkfiles(
            "./compressionmethods/LZWHUFFMAN/decodedLZWHUFFMAN"+file, "./dataset/"+file)

        #
        #
        #
        #
        #
        #
        # MTF+HUFF
        start = time.time()
        MTFHUFF.encodemtfhuff(file, data, alfabeto)
        end = time.time()
        print(f"ENCODE MTF+HUFF: {end-start:.5f} segundos")
        MTFHUFF.decodemtfhuff(file, alfabeto)
        end = time.time()
        print(f"DECODE MTF+HUFF: {end-start:.5f} segundos")

        compressedfilesize = os.stat(
            "./compressionmethods/MTFHUFF/" +
            file.split(".")[0]+".LZWhuffData").st_size + os.stat(
            "./compressionmethods/MTFHUFF/" +
            file.split(".")[0]+".LZWhuffTable").st_size

        filesize = os.stat(
            "./compressionmethods/MTFHUFF/decodedMTFHUFF"+file).st_size

        compressionrate = calcrate(tamanhooriginal, compressedfilesize)

        DataInfo.printinfo(tamanhooriginal, filesize,
                           compressedfilesize, compressionrate)

        checkfiles(
            "./compressionmethods/MTFHUFF/decodedMTFHUFF"+file, "./dataset/"+file)

        #
        #
        #
        #
        # BZIP2
        with open("./dataset/"+file, "rb") as fh:
            data = fh.read()
        fh.close()  # read data in binary

        start = time.time()
        encoded = BZIP2.compress(data)
        end = time.time()

        BZIP2.writetofile(
            "./compressionmethods/BZIP2/"+file.split(".")[0]+".bzip2", encoded)

        print(f"ENCODE BZIP2: {end-start:.5f} segundos")

        decoded = BZIP2.decompress(encoded)
        end = time.time()

        BZIP2.writetofile(
            "./compressionmethods/BZIP2/decodedBZIP2"+file, decoded)

        print(f"DECODE BZIP2: {end-start:.5f} segundos")

        compressedfilesize = os.stat(
            "./compressionmethods/BZIP2/"+file.split(".")[0]+".bzip2").st_size
        filesize = os.stat(
            "./compressionmethods/BZIP2/decodedBZIP2"+file).st_size
        compressionrate = calcrate(tamanhooriginal, compressedfilesize)

        DataInfo.printinfo(tamanhooriginal, filesize,
                           compressedfilesize, compressionrate)


def calcrate(originalfilesize, compressedfilesize):
    compressionrate = ((originalfilesize-compressedfilesize) /
                       originalfilesize)*100
    return compressionrate


def checkfiles(PATH1, PATH2):
    # check where the given files are different
    with open(PATH1, "r") as f:
        lido1 = f.readlines()
        f.close()

    with open(PATH2, "r") as f2:
        lido2 = f2.readlines()
        f2.close()

    hashedfirst = hash(frozenset(lido1))
    hashedsecond = hash(frozenset(lido2))
    # print(hashedfirst)
    # print(hashedsecond)
    if hashedfirst == hashedsecond:
        print("Ficheiro descomprimido e original iguais\n\n")
    else:
        print("########################## Ficheiro descomprimido e original diferentes ##############################")
        sys.exit(1)


if __name__ == "__main__":
    main()
