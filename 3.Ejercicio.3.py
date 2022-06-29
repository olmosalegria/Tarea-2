#Escribir una función que calcule el área de un círculo y 
# otra que calcule el volumen de un cilindro usando la
#  primera función.

def area_circulo(diametro):
     area=(3.141592 * (diametro **2))/ 4
     return area
# volumen cilindro
def volumen_cilindro(altura, radio):
    volumen =3.141592*(radio ** 2)*altura
    return volumen

def main():
    print(area_circulo(6))
    print(volumen_cilindro(2,6))
if __name__ == '__main__':
    main()

