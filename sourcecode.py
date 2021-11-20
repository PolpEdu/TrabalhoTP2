import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

# importing codecs
#import HuffmanCODEC

FILES = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]


def main():
    for file in FILES:

        print(file)
        [data, alfabeto] = read(file)
        print("Tamanho:"+str(len(data)))

        ocorrencias = get_ocorrencias(data, alfabeto)
        # limite mínimo teórico para o número médio de bits por símbolo
        print(
            f"Entropia de {file}: {entropia(ocorrencias):.5f} bits/simbolo")

        # criarhist(ocorrencias, alfabeto)

        print(
            f"No pior dos casos codificavamos {file} com: {piorCodec(alfabeto):.5f} bits/simbolo\n\n")
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


def piorCodec(alfabeto):
    nrbitssimb = np.log2(len(alfabeto))
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
