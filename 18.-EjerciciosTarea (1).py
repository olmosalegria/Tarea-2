#Escribir funcion que calcule el area de un circulo y el volumen
# de un cilindro usando la primera funcion
def area_circulo(diametro):
     area=(3.141592 * (diametro **2))/ 4
     return area
# volumen cilindro
def volumen_cilindro(altura, radio):
    volumen =3.141592*(radio ** 2)*altura
    return volumen

def main():
    print(area_circulo(5))
    print(volumen_cilindro(2,5))
if __name__ == '__main__':
    main()