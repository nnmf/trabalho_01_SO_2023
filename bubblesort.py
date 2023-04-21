from util import *
import time


def verificacaoBubble(tranca):
    sair = True
    while verif_vazio("./numeros/num.txt") == sair:
        print("Bubble Sort esta aguarando o txt ter numeros\n")
    tranca.acquire()
    print("Iniciando Bubble Sort\n")
    tranca.release()
    vet = ler_vetor('./numeros/num.txt')
    start = time.time()
    bubble_sort(vet)
    end = time.time()
    tranca.acquire()
    print('\n-----------------------')
    print("Finalizado Merge Sort\n")
    print(f"O Bubble Sort demorou: {end - start} segundos. Aqui está o print dele organizado:\n")
    print(vet)
    print('-----------------------\n')
    tranca.release()


def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

