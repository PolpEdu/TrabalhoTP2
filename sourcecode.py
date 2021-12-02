
import os
import compressionmethods.RLE as RLE
import compressionmethods.MTF.MoveToFront as MTF
import compressionmethods.LZW.LZW as LZW
import filecmp
from DataInfo import *

FILES = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]


def main():
    # escrever os dados num arquivo byte-wise
    for file in FILES:

        print("Nome: "+file)
        data, alfabeto = read(file)
        print("Tamanho data: "+str(len(data)) +
              ", tamanho alfabeto: "+str(len(alfabeto)))

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
        # Move to front
        MTF.move2front_encode(file, data, alfabeto)
        MTF.move2front_decode(file, alfabeto)
        print(filecmp.cmp("bible.txt", "./dataset/bible.txt"))


        #
        #
        #
        #
        # HUFFMAN CODEC - COMPRIMIR PAR AUM FICHEIRO (A BIT STREAM DATA) e depois ver quanto é q ele ocupa.
        #symbols, length = huffmancodec(data)
        # print(f"Codificamos {file} com: {symbols} e {length}")

        #print(
        #    f"Número médio de bits de {file} com codificação de Huffman: {DataInfo.nrmediobitsHuffman(length, symbols, ocorrencias, alfabeto):.5f} bits/simbolo")

        #
        #
        #
        # 8 BITS - DATA SET COM 2^8 ENTRADAS
        # MAX_WIDTH não pode ser maior que 16 porque 2*8 = 16 bits
        # LZW CODEC
        MAX_WIDTH = 12
        LZW.compress(file, data, MAX_WIDTH)
        LZW.decompress(file)

        #print(
        #    f"Número médio de bits de {file} com codificação LZ78: {DataInfo.bitssimbolo(len(dictionary)):.5f} bits/simbolo")

        #
        #
        #
        #
        # RLE CODEC
        # dataRLEcompressed = compressRLE(data)
        # print(
        #    f"Número médio de bits de {file} com codificação LZ78: {DataInfo.nr():.5f} bits/simbolo")

        print("\n")
    return


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


def huffmancodec(data):
    codec = HuffmanCodec.from_data(data)
    symbols, lenghts = codec.get_code_len()
    return symbols, lenghts



if __name__ == "__main__":
    main()
