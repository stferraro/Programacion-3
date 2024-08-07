'''Ejercicio 1: Cálculo de Descuento en una Tienda escribe 
Un programa que solicite al usuario el precio original de un artículo y el porcentaje de descuento. Luego, 
el programa debe calcular y mostrar el precio final después de aplicar el descuento.'''

precio_original = float(input('Introduce el precio original: '))
porcentaje_descuento = float(input('Introduce el porcentaje de descuento: '))

descuento = (precio_original * porcentaje_descuento) / 100
precio_final = precio_original - descuento

print(f'El precio final es: {precio_final:.2f}')
