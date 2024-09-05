'''Aplicacion en python que calcula el IMC de una persona'''

peso = float(input('Introduce tu peso en kg: '))
estatura = float(input('Introduce tu estatura en m: '))

imc = peso / (estatura ** 2)
imc2 = round(peso / (estatura ** 2), 2)

print(f'Tu IMC es: {imc:.2f}')
print(format('Tu IMC es: ' + imc, '.2f')) #otra forma de imprimir el imc)
print(f'Tu IMC es: {imc2}')