import threading
from bubblesort import *
from matrizes import *
from mergesort import *


def iniciar_programa():
    # utilizo das trancas (Lock) para ter um print mais "entendível", já que, por serem vários processos ao mesmo
    # tempo, pode ocorrer um bug na hora de printar
    tranca = threading.Lock()
    R = threading.Thread(target=print_matrizes, args=(tranca,))
    P = threading.Thread(target=verificacaoBubble, args=(tranca,))
    A = threading.Thread(target=verificacaoMerge, args=(tranca,))

    # Inicio as execuções das threads
    R.start()
    P.start()
    A.start()

    # Faço com que o programa continue apenas quando todas as execuções acabarem
    R.join()
    P.join()
    A.join()

    apagar_txt("./numeros/num.txt")


def main():
    print("\n----- Iniciado -----\n")
    iniciar_programa()
    print("\n----- Terminado -----\n")


if __name__ == '__main__':
    main()
