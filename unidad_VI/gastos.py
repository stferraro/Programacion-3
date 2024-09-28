gastos={}


nombre = input('Introduce tu nombre: ')
salario = float (input('Salario mensual: '))

gasto = input('Introduce el gasto: ')
while gasto != 'Fin':

    valor = float(input('Valor: '))
    while valor < 0:
        print('Introduce un valor positivo')
        valor = float(input('Valor: '))

    gastos[gasto] = valor
    gasto = input('Introduce el gasto: ')

else:

    print(gastos)
    gasto_max = max(gastos, key=gastos.get)
    print(f'El gasto mas caro del mes es: {gasto_max} y tiene el valor de {gastos.get(gasto_max):.2f}')
    gasto_min = min(gastos, key=gastos.get)
    print(f'El gasto mas bajo del mes es: {gasto_min} y tiene el valor de {gastos.get(gasto_min):.2f}')
    print(f'El total de todos los gastos es: {sum(gastos.values()):.2f}')
    suma_gastos = sum(gastos.values())
    if suma_gastos > salario:
        print('Debes ahorrar te quedastes sin dinero')
