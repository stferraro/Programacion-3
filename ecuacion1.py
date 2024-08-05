'''escribir un programa que resuelve ecuaciones de segundo grado
del tipo ax^2 + bx + c = 0
'''

import math

a = float(input('Introduce el valor de a: '))
b = float(input('Introduce el valor de b: '))
c = float(input('Introduce el valor de c: '))

determinante = (b**2) - (4*a*c)

if determinante > 0:
    x1 = ((-1 * b) + (math.sqrt(determinante)) )/ (2*a)
    x2 = ((-1* b) - (math.sqrt(determinante))) / (2*a)
    print(f'Las soluciones son {x1:.2f} y {x2:.2f}')
if determinante == 0:
    x = (-1*b) / (2*a)
    print(f'La solucion es {x:.2f}')
if determinante < 0:
    print('La ecuacion no tiene soluciones reales')