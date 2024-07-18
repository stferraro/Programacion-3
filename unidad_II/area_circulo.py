'''aplicacion en python que calcula el area de un circulo'''

import math

diametro = float(input('Introduce el diametro del circulo: '))

radio = diametro / 2
PI = 3.1416

area = math.pi * (radio ** 2)
area_circulo = (radio ** 2) * PI


print(f'El area del circulo es: {area:.2f}')
print(f'El area del circulo es: {area_circulo:.2f}')