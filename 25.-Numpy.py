#NUMPY

#Que es numpy?
#Libreria para el calculo numerico y manejo de arreglos ( array)
#listas organizadas de numeros
#mas veloz y eficiente para manejar listas/arreglos en python
#agrega soporte para grandes arreglos, multidimensionales y matrices.

#como se instala:
# en la consola activar ambiente virtual de miniconda
#pip install numpy
#https://numpy.org/install/


# Como importar 
# import numpy as np 

import numpy as np
def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print(lista)

    # crear un arreglo
    arreglo = np.array(lista)
    print(arreglo)
    print(type(arreglo))

    #crear arreglo de dos dimensiones
    matriz= np.array([[1,2,3], [4,5,6] , [7,8,9]])
    print(matriz)

    #indexacion de arreglos
    print(arreglo[0])
    print(arreglo[0] + arreglo [1])

    # indexacion de matrices
    print(matriz [0])
    print(matriz [0,0])
    print(matriz[0,0] + matriz [0,0])

    print( arreglo [0:3])


   
    


if __name__== '__main__':
    main()
