from util import *
import time

from util import ler_vetor


def verificacaoMerge(tranca):
    sair = True
    while verif_vazio("./numeros/num.txt") == sair:
        print("Merge Sort esta aguarando o txt ter numeros\n")

    tranca.acquire()
    print("Iniciando Merge Sort\n")
    tranca.release()
    vet = ler_vetor('./numeros/num.txt')
    start = time.time()
    merge_sort(vet)
    end = time.time()
    tranca.acquire()
    print('\n-----------------------')
    print("Finalizado Merge Sort\n")
    print(f"O Merge Sort demorou: {end - start} segundos. Aqui está o print dele organizado:\n")
    print(vet)
    print('-----------------------\n')
    tranca.release()


def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left_half = lista[:mid]
        right_half = lista[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lista[k] = left_half[i]
                i += 1
            else:
                lista[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lista[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lista[k] = right_half[j]
            j += 1
            k += 1
