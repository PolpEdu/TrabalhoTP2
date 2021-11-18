import numpy as np
import matplotlib.pyplot as plt
import os

FILES = ["bible.txt","finance.csv","jquery-3.6.0.js", "random.txt"]


def main():
    [data, alfabeto] = read(FILES[0])
    ocorrencias = get_ocorrencias(data, alfabeto)
    print(f"\nEntropia de {FILES[0]}: {entropia(ocorrencias):.5f} bits/simbolo")
    
    return



def read(filename): 
    PATH = os.getcwd()+"\\TrabalhoTP2\\dataset\\" + filename
    ext = filename.split(".")[1]

    if ext == "txt":
       

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

    return data, alfabeto

# get ocorrencias da data
def get_ocorrencias(data, alfabeto):
    # print(data)
    ocorrencias = np.zeros(len(alfabeto))
    for x in data:
        ocorrencias[alfabeto.index(ord(x))] += 1
    return ocorrencias
    

def entropia(ocorrencias):
    ocorrencias = np.array(ocorrencias)
    p = ocorrencias[ocorrencias > 0] / np.sum(ocorrencias)
    H = np.sum(p * np.log2(1 / p))
    # print(f"\n{H:.5f} bits/simbolo")
    return H 

def criarhist(ocorrencias, alfabeto):
    # print(ocorrencias)
    # ppapra aparecer todos:
    # plt.xticks(range(len(ocorrencias)), alfabeto)

    wh = (14, 8)
    plt.figure(figsize=wh)
    plt.bar(alfabeto, ocorrencias, ec="k")

    plt.xlabel('Alfabeto', fontsize=15)
    plt.ylabel('Ocorrencias', fontsize=15)
    plt.show()

if __name__=="__main__":
    main()