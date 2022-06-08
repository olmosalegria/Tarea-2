#Ejercicio 1: Escribir un programa en el que se pregunte al
#  usuario por una frase y una letra, y muestre por pantalla
#  el número de veces que aparece la letra en la frase. 

frase = input("Ingresa una frase: ")
letra = input("Ingresa una letra: ")
contador = 0
for letra in frase:
	if letra == letra:
	    contador = contador + 1
	

print("La letra" + letra_a_buscar + "aparece" + str(contador))
