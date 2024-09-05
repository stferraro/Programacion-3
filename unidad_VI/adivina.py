import random

numero = random.randint(1, 100)

print('Adivina el numero')

while True:
    entrada = int(input())
    
    while entrada < 1 or entrada > 100:
        print('Introduce un numero entre 1 y 100')
        entrada = int(input())
        

    if entrada < numero:
        print('Mas alto')
    elif entrada > numero:
        print('Mas bajo')
    else:
        print('Enhorabuena')
        print(f'El numero era {numero}')
        break
    