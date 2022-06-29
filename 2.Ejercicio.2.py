#Ejercicio 2 (30 puntos): Escriba un programa 
# que pida dos palabras y diga si riman o no.
#  Si coinciden las últimas tres letras tiene que decir que riman.
#  Si coinciden sólo las últimas dos tiene que decir que riman un poco.
#  Y si no coinciden, decir que no riman. Validar que las palabras
#  tengan al menos tres letras. Nota: Utilizar slices

primera_palabra= input("Ingrese la primera palabra: ")
segunda_palabra= input("Ingrese la segunda palabra: ")

palabra1_ultimas_tres= primera_palabra[-3:]
palabra2_ultimas_tres= segunda_palabra[-3:]

palabra1_ultimas_dos= primera_palabra [-2:]
palabra2_ultimas_dos= segunda_palabra [-2:]



if palabra1_ultimas_tres == palabra2_ultimas_tres:
    print("Las palabras riman")
elif palabra1_ultimas_dos == palabra2_ultimas_dos:
    print("Las palabran riman un poco")
else:
    print("Las palabras no riman")
