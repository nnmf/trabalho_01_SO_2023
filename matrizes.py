from util import *


def print_matrizes(tranca):
    embaralhar_numeros()
    mat1, mat2 = ler_matrizes('numeros/matrizes.txt')
    result = multicacao_de_matrizes(mat1, mat2)
    matriz_para_txt(result, './numeros/num.txt')
    vet = ler_vetor('./numeros/num.txt')
    tranca.acquire()
    print('\n-----------------------')
    print("Resultado da Matriz:")
    print(result)
    print("A Matriz num vetor para facilitar a visualização:")
    print(vet)
    print('-----------------------\n')
    tranca.release()
    apagar_txt("./numeros/matrizes.txt")



def multicacao_de_matrizes(mat1, mat2):
    result = [[0.0 for _ in range(4)] for _ in range(4)]
    n = len(mat1)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
