
import os
import compressionmethods.RLE as RLE
import compressionmethods.MTF.MoveToFront as MTF
import compressionmethods.LZW.LZW as LZW
import compressionmethods.HuffmanCODEC.huffmancodec as hf
import compressionmethods.BWT.Burrows_Wheeler as BWT
import compressionmethods.RLE.RLE as RLE
import compressionmethods.LZWHUFFMAN.lzwhuffman as LZWHUF
import compressionmethods.BWTRLE.bwtrle as BWTRLE
from DataInfo import *
import time
import sys

FILES = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]
MAX_WIDTH = 12


def main():
    # escrever os dados num arquivo byte-wise
    for file in FILES:

        print("Nome: "+file)
        data, alfabeto = read(file)
        tamanhooriginal = len(data)
        print("Tamanho data: "+str(tamanhooriginal) +
              " bytes, tamanho alfabeto: "+str(len(alfabeto)))

        ocorrencias = DataInfo.get_ocorrencias(data, alfabeto)
        # criarhist(ocorrencias, alfabeto)

        print(
            f"No pior dos casos codificavamos {file} com: {DataInfo.bitssimbolo(len(alfabeto)):.5f} bits/simbolo")

        # limite mínimo teórico para o número médio de bits por símbolo NORMAL
        print(
            f"Entropia de {file}: {DataInfo.entropia(ocorrencias):.5f} bits/simbolo")

        '''
        #
        #
        #
        #
        # Move to front
        start = time.time()
        compressedfilesize = MTF.move2front_encode(file, data, alfabeto)
        end = time.time()
        print(f"MTF encode: {end-start:.5f} segundos")

        filesize = MTF.move2front_decode(file, alfabeto)
        end = time.time()
        print(f"MTF decode: {end-start:.5f} segundos")

        compressionrate = calcrate(tamanhooriginal, compressedfilesize)
        print(f" Tamanho do ficheiro original: {tamanhooriginal} bytes\n",
              f"Tamanho do ficheiro apos a sua codificação e descodificação: {filesize} bytes\n",
              f"Tamanho do ficheiro comprimido: {compressedfilesize} bytes\n",
              f"Taxa de compressão: {compressionrate:.02f} %")

        checkfiles("./decoded/decodedMTF"+file, "./dataset/"+file)

        #
        #
        #
        #
        # HUFFMAN CODEC - COMPRIMIR PAR AUM FICHEIRO (A BIT STREAM DATA) e depois ver quanto é q ele ocupa.
        start = time.time()
        hf.Huffman_encode(data, file)
        end = time.time()
        print(f"HUFFMAN encode: {end-start:.5f}s")
        hf.Huffman_decode(file)
        end = time.time()

        tablesize = os.stat(
            './encoded/'+file.split(".")[0]+'.huffTable').st_size

        huffdata = os.stat('./encoded/'+file.split(".")[0]+'.huffData').st_size

        compressedfilesize = tablesize+huffdata

        print(f"HUFFMAN decode: {end-start:.5f} segundos")
        compressionrate = calcrate(tamanhooriginal, compressedfilesize)
        print(f" Tamanho do ficheiro original: {tamanhooriginal} bytes\n",
              f"Tamanho do ficheiro apos a sua codificação e descodificação: {filesize} bytes\n",
              f"Tamanho do ficheiro comprimido: {compressedfilesize} bytes, table size:{tablesize} bytes e tree size:{huffdata} bytes\n",
              f"Taxa de compressão: {compressionrate:.02f} %\n")

        checkfiles("./decoded/decodedHuffman"+file, "./dataset/"+file)

        # print(
        #    f"Número médio de bits de {file} com codificação de Huffman: {DataInfo.nrmediobitsHuffman(length, symbols, ocorrencias, alfabeto):.5f} bits/simbolo")

        #
        #
        #
        # 8 BITS - DATA SET COM 2^8 ENTRADAS
        # MAX_WIDTH não pode ser maior que 16 porque 2*8 = 16 bits
        # LZW CODEC
        start = time.time()

        compressed_data = LZW.compress(file, data, MAX_WIDTH)
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
        print(f" Tamanho do ficheiro original: {tamanhooriginal} bytes\n",
              f"Tamanho do ficheiro apos a sua codificação e descodificação: {filesize} bytes\n",
              f"Tamanho do ficheiro comprimido: {compressedfilesize} bytes\n",
              f"Taxa de compressão: {compressionrate:.02f} %\n")

        checkfiles("./decoded/decodedLZW"+file, "./dataset/"+file)

        # print(
        #    f"Número médio de bits de {file} com codificação LZ78: {DataInfo.bitssimbolo(len(dictionary)):.5f} bits/simbolo")

        BLOCKSIZE = 100
        start = time.time()
        encoded_BWT = BWT.encode(file, data, BLOCKSIZE)
        compressedfilesize = BWT.writetofileENC(file, encoded_BWT)
        end = time.time()
        print(f"BWT encode: {end-start:.5f} segundos")

        decoded_BWT = BWT.decode(file, BLOCKSIZE)
        filesize = BWT.writetofileDEC(file, decoded_BWT)
        end = time.time()
        print(f"BWT decode: {end-start:.5f} segundos")
        compressionrate = calcrate(tamanhooriginal, compressedfilesize)
        print(f" Tamanho do ficheiro original: {tamanhooriginal} bytes\n",
              f"Tamanho do ficheiro apos a sua codificação e descodificação: {filesize} bytes\n",
              f"Tamanho do ficheiro comprimido: {compressedfilesize} bytes\n",
              f"Taxa de compressão: {compressionrate:.02f} %\n")

        checkfiles("./decoded/decodedBWT"+file, "./dataset/"+file)

        #
        #
        #
        #
        # RLE CODEC
        start = time.time()
        encoding_RLE = RLE.compressRLE(file, data)
        compressedfilesize = RLE.writetofileENC(file, encoding_RLE)
        end = time.time()
        print(f"RLE encode: {end-start:.5f} segundos")

        decoded_RLE = RLE.decompressRLE(file)
        filesize = RLE.writetofileDEC(file, decoded_RLE)
        end = time.time()
        print(f"RLE decode: {end-start:.5f} segundos")

        compressionrate = calcrate(tamanhooriginal, compressedfilesize)

        print(f" Tamanho do ficheiro original: {tamanhooriginal} bytes\n",
              f"Tamanho do ficheiro apos a sua codificação e descodificação: {filesize} bytes\n",
              f"Tamanho do ficheiro comprimido: {compressedfilesize} bytes\n",
              f"Taxa de compressão: {compressionrate:.02f} %\n")

        checkfiles("./decoded/decodedRLE"+file, "./dataset/"+file)

        #
        #
        #
        #
        #
        #
        # lzw+huffman
        start = time.time()
        LZWHUF.lzwHuffmanenc(file, data)
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
        print(f" Tamanho do ficheiro original: {tamanhooriginal} bytes\n",
              f"Tamanho do ficheiro apos a sua codificação e descodificação: {filesize} bytes\n",
              f"Tamanho do ficheiro comprimido: {compressedfilesize} bytes\n",
              f"Taxa de compressão: {compressionrate:.02f} %\n")

        checkfiles(
            "./compressionmethods/LZWHUFFMAN/decodedLZWHUFFMAN"+file, "./dataset/"+file)
'''
        #
        #
        #
        #
        #
        #
        # BWT+RLE
        start = time.time()
        BLOCKSIZERLE = 100
        BWTRLE.bwtrleenc(file, data, BLOCKSIZERLE)
        end = time.time()
        print(f"ENCODE BWT+RLE: {end-start:.5f} segundos")
        BWTRLE.bwtrledec(file)
        end = time.time()
        print(f"DECODE: BWT+RLE: {end-start:.5f} segundos")

        compressedfilesize = os.stat(
            "./compressionmethods/BWTRLE/" +
            file.split(".")[0]+".bwtrle").st_size

        filesize = os.stat(
            "./compressionmethods/BWTRLE/decodedBWTRLE"+file).st_size

        compressionrate = calcrate(tamanhooriginal, compressedfilesize)
        print(f" Tamanho do ficheiro original: {tamanhooriginal} bytes\n",
              f"Tamanho do ficheiro apos a sua codificação e descodificação: {filesize} bytes\n",
              f"Tamanho do ficheiro comprimido: {compressedfilesize} bytes\n",
              f"Taxa de compressão: {compressionrate:.02f} %\n")

        checkfiles(
            "./compressionmethods/BWTRLE/decodedBWTRLE"+file, "./dataset/"+file)


def calcrate(originalfilesize, compressedfilesize):
    compressionrate = ((originalfilesize-compressedfilesize) /
                       originalfilesize)*100
    return compressionrate


def read(filename):
    PATH = os.getcwd()+"\\dataset\\" + filename

    with open(PATH, "r", encoding="ASCII") as f:
        lido = f.readlines()
        data = ""

        for x in lido:
            data += x

        f.close()

    # calcular o alfabeto ideal  com virgulas e pontos finais e letras do alfabeto grego normais.
    alfabeto = []
    for x in data:
        if x not in alfabeto:
            alfabeto.append(x)
    alfabeto.sort()
    return data, alfabeto

# get ocorrencias da data


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
        print("Ficheiro descomprimido e original diferentes\n\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
