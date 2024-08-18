saldo_promedio = float(input('Introduce el saldo promedio:  '))
cantidad_años = int(input('Introduce la cantidad de años:  '))

tipo_cliente = ' '

if saldo_promedio >= 50000 and cantidad_años >= 10:
    tipo_cliente = 'Cliente Platino'
    saldo = (saldo_promedio + (saldo_promedio * 2 / 100))
elif saldo_promedio >= 20000 and cantidad_años >= 5:
    tipo_cliente = 'Cliente Oro'
    saldo = (saldo_promedio + (saldo_promedio * 1 / 100))
elif saldo_promedio < 5000:
    tipo_cliente = 'Cliente Regular'
    saldo = (saldo_promedio + (saldo_promedio * 0.5 / 100))

print(f'El tipo de cliente es: {tipo_cliente}')
print(f'El nuevo saldo es: {saldo:.2f}')dddd