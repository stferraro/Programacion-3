monto_total = float(input('Introduce el monto total:  '))
monto_final = 0

if monto_total >= 1000:
    monto_final = monto_total - (monto_total * 0.10)
elif monto_total >= 500 and monto_total < 1000:
    monto_final = monto_total - (monto_total * 0.05)
else :
    monto_final = monto_total
    
print(f'El total a pagar es: {monto_final:.2f}')
    