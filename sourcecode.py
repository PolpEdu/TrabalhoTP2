import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
from huffmancodec import *
from LZ78 import *
from RLE import *


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


class DataInfo:
    def nrmediobitsLZ78():
        return

    def nrmediobitsHuffman(length, symbols, ocorrencias, alfabeto):
        # criar uma lista com o mesmo tamanho das ocorrencias
        novasocoreencias = [0] * len(symbols)
        numerador = 0
        i = 0

        # contar as ocorrencias de cada simbolo na fonte
        for x in range(len(alfabeto)):
            if i != len(symbols):  # para não dar overflow
                if alfabeto[x] == symbols[i]:  # se os simbolos tiverem o alfabeto
                    # adiciono a ocorrencia
                    novasocoreencias[i] = ocorrencias[x]
                    i += 1

        for x in range(len(symbols)):
            # contagens da media normal
            numerador += length[x] * novasocoreencias[x]

        denominador = np.sum(novasocoreencias)

        E = numerador / denominador

        return E

    def get_ocorrencias(data, alfabeto):
        # print(data)
        ocorrencias = np.zeros(len(alfabeto))
        for x in data:
            ocorrencias[alfabeto.index(x)] += 1
        return ocorrencias

    def entropia(ocorrencias):
        ocorrencias = np.array(ocorrencias)
        p = ocorrencias[ocorrencias > 0] / np.sum(ocorrencias)
        H = np.sum(p * np.log2(1 / p))
        # print(f"\n{H:.5f} bits/simbolo")
        return H

    def bitssimbolo(alfabetolen):
        nrbitssimb = np.log2(alfabetolen)
        return nrbitssimb

    def criarhist(ocorrencias, alfabeto):
        # print(ocorrencias)
        # ppapra aparecer todos:
        # plt.xticks(range(len(ocorrencias)), alfabeto)

        wh = (14, 8)
        matplotlib.rcParams.update(
            {
                'text.usetex': False,
                'font.family': 'stixgeneral',
                'mathtext.fontset': 'stix',
            }
        )
        plt.figure(figsize=wh)
        plt.bar(alfabeto, ocorrencias, ec="k")

        plt.xlabel('Alfabeto', fontsize=15)
        plt.ylabel('Ocorrencias', fontsize=15)
        plt.show()


if __name__ == "__main__":
    main()
