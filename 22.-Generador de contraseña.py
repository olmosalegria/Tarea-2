#Generador de contraseña

import random

def generar_contrasena():
    mayusculas = ['A', 'B' , 'C' , 'D' , 'E' , 'F']
    minusculas = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    simbolos = ['#', '$', '%' , '&' , '/']

    caracteres= mayusculas + minusculas + numeros + simbolos 
    contrasena = []

    for i in range (15): # este for recorre 15 veces
        caracter_aleatorio = random.choice (caracteres) # escoge un carcater
        contrasena.append(caracter_aleatorio) # append para agregar la contraseña a la lista
    
    # Convertir lista a string
    # " o '' simbolizan un string vacio
    # . join accedemos al metodo join

    contrasena= 'hola'.join(contrasena) #transforma lista a print , quita corchetes comas etc
    
    return contrasena

def main():
    contrasena = generar_contrasena ()
    print("su contraseña es: " + contrasena)


if __name__== '__main__':
    main()
