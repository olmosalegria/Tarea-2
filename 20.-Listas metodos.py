#Lista metodos

def main():
  #  numeros= [1,3,5,7,8,9,0]
  #  print( type(numeros) )
  #  print( numeros[4] )

    objetos = ['hola', 2,4,5, True]
    print (objetos[3])

    #agregar elementos
    objetos.append(False)
    print(objetos)

    objetos.append(45) # append sirve para agregar mas datos a la lista
    objetos.append("hola mundo")
    print(objetos)

    #eliminar elementos
    objetos.pop(0)    #eliminando indice 0 , si no se pone el cero, elimina el ultimo objeto de la lista
    print(objetos)

    #recorrer lista
    for objeto in objetos:
        print(objeto)  #hace un print de cada valor
    
    #ordenar lista

    print(objetos[::-1])

    #sumar listas
    numero_1= [1,2,3]
    numero_2=[4,5,6]
    lista_final=numero_1 + numero_2
    print(lista_final)


if __name__== '__main__':
    main()
