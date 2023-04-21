import random
import os


def embaralhar_numeros():
    # limpa as matrizes caso tenha iniciado-as antes
    op = './numeros/matrizes.txt'
    apagar_txt(op)

    # Abrir arquivo de entrada e ler os números
    with open("numeros/entrada.txt", "r") as f:
        numeros = f.read().split()

    # Embaralhar os números
    random.shuffle(numeros)

    # Escrever os números embaralhados no arquivo de saída
    with open("numeros/matrizes.txt", "w") as f:
        for i in range(len(numeros)):
            f.write(numeros[i])
            if i % 4 == 3:
                f.write("\n")
            else:
                f.write(" ")


def matriz_para_txt(mat, op):
    with open(op, "w") as f:
        linha = ""
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                linha += str(mat[i][j]) + " "
        f.write(linha)


def ler_matrizes(op):
    with open(op, 'r') as f:
        # ler a primeira matriz
        mat1 = []
        for i in range(4):
            l = list(map(float, f.readline().strip().split()))
            mat1.append(l)

        # ler a segunda matriz
        mat2 = []
        for i in range(4):
            l = list(map(float, f.readline().strip().split()))
            mat2.append(l)

    return mat1, mat2


def ler_vetor(op):
    with open(op, 'r') as f:
        numeros = []
        linha = f.readline()
        while linha:
            numeros += [float(num) for num in linha.split()]
            linha = f.readline()
        return numeros


def apagar_txt(op):
    with open(op, 'w') as arquivo:
        arquivo.truncate()


# verifica se o arquivo está vazio
def verif_vazio(op):
    return os.path.getsize(op) == 0
