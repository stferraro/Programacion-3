'''Ejercicio 4: Porcentaje de Participación en una Encuesta
Una encuesta realizada a 1,000 personas tiene los siguientes resultados: 
300 personas votaron por la opción A, 
450 por la opción B, y 250 por la opción C. 
Escribe un programa que calcule y muestre el porcentaje de personas que votaron por cada opción respecto al total de encuestados.'''

total_encuestados = 1000
total_a = 300
total_b = 450
total_c = 250

porcentaje_a = (total_a * 100) / total_encuestados
porcentaje_b = (total_b * 100) / total_encuestados
porcentaje_c = (total_c * 100) / total_encuestados

print(f'El porcentaje de personas que votaron por A es: {porcentaje_a:.2f}%')
print(f'El porcentaje de personas que votaron por B es: {porcentaje_b:.2f}%')
print(f'El porcentaje de personas que votaron por C es: {porcentaje_c:.2f}%')