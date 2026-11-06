import math
num=float(input("Introduce un número: "))
def cuadrado_raiz(num):
    cuadrado=num**2
    raiz=math.sqrt(num)
    return cuadrado,raiz
cuadr,raiz=cuadrado_raiz(num)
print(f'El cuadrado de el número es {cuadr} y su raíz es {raiz}')