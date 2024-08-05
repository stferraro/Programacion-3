costo_pan = 3.49
porcentaje_descuento = 0.60

num_pan_hoy = int(input('Introduce el numero de panes vendidos hoy: '))
num_pan_viejo = int(input('Introduce el numero de panes de ayer: '))

precio_con_descuento =costo_pan - (costo_pan * porcentaje_descuento) 

total = (num_pan_hoy * costo_pan) + (num_pan_viejo * precio_con_descuento)


print(f'El total a pagar es: {total:.2f}')


