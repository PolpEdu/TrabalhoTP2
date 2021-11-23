
import os
from huffmancodec import *
from LZ78 import *
from RLE import *
import DataInfo

FILES = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]


def main():
    test()
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
        # HUFFMAN CODEC
        symbols, length = huffmancodec(data)
        # print(f"Codificamos {file} com: {symbols} e {length}")

        print(
            f"Número médio de bits de {file} com codificação de Huffman: {DataInfo.nrmediobitsHuffman(length, symbols, ocorrencias, alfabeto):.5f} bits/simbolo")

        #
        #
        #
        #
        # LZ78 CODEC
        encodedNumbers, encodedLetters, dictionary = compressLZ78(data)
        # print("len alf: "+str(len(dictionary))) (menor que a len da data)

        print(
            f"Número médio de bits de {file} com codificação LZ78: {DataInfo.bitssimbolo(len(dictionary)):.5f} bits/simbolo")

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
