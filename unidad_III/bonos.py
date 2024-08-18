tiempo_empresa = int(input('Introduce el tiempo de la empresa:  '))
tipo_desepeño = input('Desempeño en la empresa:  ')
salario = float(input('Introduce el salario del empleado:  '))

bono = 0

if tiempo_empresa >= 5 and tipo_desepeño == 'Excelente':
    bono = 20
    salario = salario + (salario * bono / 100)
elif tiempo_empresa < 5 and tiempo_empresa >= 3 and tipo_desepeño == 'Bueno':
    bono = 10
    salario = salario + (salario * bono / 100)
elif tiempo_empresa < 3 and tipo_desepeño == 'Regular':
    bono = 5
    salario = salario + (salario * bono / 100)
else:
    bono = 0
    salario = salario + (salario * bono / 100)

print(f'El nuevo salario es: {salario:.2f}')    