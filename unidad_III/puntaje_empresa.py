puntuacion_empleado = float(input('Introduce la puntuacion del empleado:  '))

cantidad_dinero = 2400.00

if puntuacion_empleado == 0.0:
    cantidad_total = cantidad_dinero * puntuacion_empleado

elif puntuacion_empleado == 0.4:
    cantidad_total = cantidad_dinero * puntuacion_empleado

elif puntuacion_empleado >= 0.6:
    cantidad_total = cantidad_dinero * puntuacion_empleado

print(f'La cantidad total a pagar es: {cantidad_total:.2f}')