'''Ejercicio 2: Porcentaje de Aprobados 
Escribe un programa que lea la cantidad total de estudiantes y la cantidad de estudiantes que aprobaron un examen. 
El programa debe calcular y mostrar el porcentaje de estudiantes que aprobaron el examen.'''

cantidad_total_estudiantes = int(input('Introduce la cantidad total de estudiantes: '))
aprobados = int(input('Introduce la cantidad de aprobados: '))

porcentaje_aprobados = (aprobados * 100) / cantidad_total_estudiantes

print(f'El porcentaje de aprobados es: {porcentaje_aprobados:.2f}%')