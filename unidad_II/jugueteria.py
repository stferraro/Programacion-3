PESO_PAYASO = 112
PESO_MUNECA = 75

num_payasos = int(input('Introduce el numero de payasos: '))
num_munecas = int(input('Introduce el numero de munecas: '))

precio_munecas = float(input('Introduce el precio de las munecas: '))
precio_payasos = float(input('Introduce el precio de los payasos: '))

costo_payaso = num_payasos * precio_payasos
costo_muneca = num_munecas * precio_munecas

peso_total = (num_payasos * PESO_PAYASO) + (num_munecas * PESO_MUNECA)

total = (costo_muneca + costo_payaso)
total_iva = total + (total * 0.16)
total_flete = total_iva + (total_iva * 0.10) * peso_total
print(f'El total a pagar es: {total_iva:.2f}')
print(f'El total del flete es: {total_flete:.2f}')
print(f'El total a pagar es: {(total_flete + total_iva):.2f}')
print(f'peso total: {peso_total:.2f}')
