import numpy as np
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


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

