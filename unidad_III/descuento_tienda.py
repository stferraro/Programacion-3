monto_total = float(input('Introduce el monto total:  '))

if monto_total >= 1000:
    descuento = 15
elif monto_total >= 500 and monto_total < 1000:
    descuento = 10
elif monto_total >= 200 and monto_total < 500:
    descuento = 5
else:
    descuento = 0
    
total = monto_total - (monto_total * (descuento / 100))

print(f'El total a pagar     es: {total:.2f}')