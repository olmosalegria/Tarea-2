#import random as rd

import random

def main():
    #rd.randint()
    numero_aleatorio= random.randint(1,100)
    print(numero_aleatorio)   

    lista_numeros = [1,2,3,4,5,6,7]
    numero_aleatorio= random.choice( lista_numeros ) #choice escoge un elemento de la lista
    print(numero_aleatorio)

if __name__== '__main__':
    main()

