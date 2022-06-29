#dimensiones

import numpy as np


def main():
    #escalar
    escalar= np.array(42)
    print(escalar)
    print(escalar.ndim)

    #vector
    vector= np.array(42)
    print(vector)
    print(vector.ndim)

    #Matriz
    matriz= np.array([[1,2,3], [4,5,6]])
    print(matriz)

    #Tensor
    tensor= np.array([[[1,2,3], [4,5,6]],[[7,8,9],[10,11,12,]]])
    print(tensor)
if __name__== '__main__':
    main()



