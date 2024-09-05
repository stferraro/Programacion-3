'''Ejercicio 3: Porcentaje de Ingresos
Un empresario desea conocer qué porcentaje de sus ingresos mensuales proviene de cada una de sus tres fuentes principales: ventas de productos, servicios y consultoría.
Escribe un programa que pida al usuario los ingresos de cada fuente y el ingreso total. El programa debe calcular 
y mostrar el porcentaje que representa cada fuente respecto al total de ingresos.'''

ingreso_ventas = float(input('Introduce el ingreso de ventas en $: '))
ingreso_servicios = float(input('Introduce el ingreso de servicios en $: '))
ingreso_consultoria = float(input('Introduce el ingreso de consultoria en $: '))

ingreso_total = ingreso_ventas + ingreso_servicios + ingreso_consultoria

porcentaje_ventas = (ingreso_ventas * 100) / ingreso_total
porcentaje_servicios = (ingreso_servicios * 100) / ingreso_total
porcentaje_consultoria = (ingreso_consultoria * 100) / ingreso_total

print(f'El porcentaje de ventas es: {porcentaje_ventas:.2f}%')
print(f'El porcentaje de servicios es: {porcentaje_servicios:.2f}%')
print(f'El porcentaje de consultoria es: {porcentaje_consultoria:.2f}%')
print(f'El ingreso total es de: {ingreso_total:.2f} $')