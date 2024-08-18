ventas_producto = float(input('Introduce las ventas del producto:  '))
ventas_mes = float(input('Introduce las ventas del mes:  '))

porcentaje = (100 * ventas_mes) / ventas_producto

if porcentaje <= 30 :
    cantidad_producto = ventas_producto - (ventas_producto * 0.20)
elif porcentaje >= 20:
    cantidad_producto = ventas_producto + (ventas_producto * 0.30)
else:
    cantidad_producto = ventas_producto
    
print(f'La cantidad de producto es: {cantidad_producto:.2f}')    