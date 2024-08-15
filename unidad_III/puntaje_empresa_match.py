puntuacion_empleado = float(input('Introduce la puntuacion del empleado:  '))

cantidad_dinero = 2400.00

match puntuacion_empleado:
    case 0.0:
        cantidad_total = cantidad_dinero * puntuacion_empleado
    case 0.4:
        cantidad_total = cantidad_dinero * puntuacion_empleado
    case _ if puntuacion_empleado >= 0.6:
        cantidad_total = cantidad_dinero * puntuacion_empleado
    case _:
        print('La puntuacion no es valida')

print(f'La cantidad total a pagar es: {cantidad_total:.2f}')