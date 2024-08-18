nota_1 = float(input('Introduce la nota 1:  '))
nota_2 = float(input('Introduce la nota 2:  '))
nota_3 = float(input('Introduce la nota 3:  '))
nota_4 = float(input('Introduce la nota 4:  '))
nota_5 = float(input('Introduce la nota 5:  ')) 

promedio = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5
valor_promedio = ' '

if promedio >= 90:
    valor_promedio = 'Excelente'
elif promedio < 90 and promedio >= 80:
    valor_promedio = 'Moderado'
elif promedio < 80 and promedio >= 70:
    valor_promedio = 'Bueno'
elif promedio < 70 and promedio >= 60:
    valor_promedio = 'Aceptable'
else:
    valor_promedio = 'Suficiente'

print(f'El promedio es: {promedio:.2f}')
print(f'El valor del promedio es: {valor_promedio}')