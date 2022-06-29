#Ejercicio 1 (30 puntos):
#  Escribir un programa que contenga una 
# función que reciba una lista de palabras y devuelva la más larga.
#  Imprimir por pantalla la palabra resultante.

# con un total de tres palabras en la lista

def palabra_mas_larga(primera_palabra, segunda_palabra , tercera_palabra):
    if len(primera_palabra) >= len (segunda_palabra) and len (primera_palabra) >= len(tercera_palabra):
        palabra = primera_palabra
    elif len(segunda_palabra) >= len(tercera_palabra):
        palabra= segunda_palabra
    else:
        palabra= tercera_palabra
    return(palabra)
print(palabra_mas_larga("computador", "teclado", "pantalla"))
print(palabra_mas_larga(" amarillo", "rojo" , "azul"))
print(palabra_mas_larga( "Hola", "adios" , "bienvenido"))





