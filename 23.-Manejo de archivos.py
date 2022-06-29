#manejo de archivos

#with: manejador contextual. Si el programa se cierra inesperadamente
# evita que se corrompa el archivo


#modos de apertura
# r Solo lectura
# r+ lectura y escritura
# w Solo escritura.Sobre escribe el archivo si existe. lo crea...
#...si no existe
#w+ Escritura y lectura.Sobrescribe el archivo si existe, lo crea si no existe
# a Añadido( agrega contenido).Crea el archivo si no existe
# a+ Añadido ( agrega contenido) y lectura. Crea el archivo si no existe.


def leer():
     numeros= []
     with open('./archivos/numeros.txt', 'r') as file:  # open para abrir archivo
         for linea in file: 
            numeros.append(int(linea))


     print( numeros )       

def escribir ():
    nombres = ['Ezequiel', 'Juan', 'Rocío', 'David']
    with open('./archivos/nombres.txt', 'a' , encoding="utf-8") as file:
        for nombre in nombres:
            file.write(nombre)
            file.write("\n") 


def main():
    escribir()

if __name__== '__main__':
    main()


