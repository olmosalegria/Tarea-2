#Ejercicio 1
#Escriba una funcion que aleatoriamente escoja un numero entero entre
#1 y 10 y lo guarde en un fichero de nombre tabla-n.txt Donde n es el 
#numero que salio. Escribir en el archivo la tabla del numero.


from random import random

import random
def main ():
    numero_aleatorio = random.randint(1, 10)
    nombre_fichero = "tabla-" + str(numero_aleatorio)+ ".txt"
    with open(nombre_fichero, "w", encoding="utf-8") as file:
        for i in range(1 , 13 ): # en vez de 13 , llegara hasta el 12 esa es la funcion de range
            linea= str(i) + "X" + str (numero_aleatorio) + "=" * str
            (numero_aleatorio + 1)

            file.write(linea)
            file.write("\n")


if __name__=='__main__':
    main()
