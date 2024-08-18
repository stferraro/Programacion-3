edad = int(input('Introduce tu edad:  '))

if edad < 4:
    costo = 0
elif 4 <= edad < 18:
    costo = 5
else:
    costo = 10

print(f'El costo de la entrada es: {costo:.2f}')