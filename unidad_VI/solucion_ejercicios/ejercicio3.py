materias = {}

nombre_alumno = input('Introduce el nombre del alumno: ')
materia = input('Introduce la materia: ')

while materia != 'n':
    
    nota = float(input('Introduce la nota: '))
    materias[materia] = nota
    
    if nota > 20 or nota < 0:
        print('Introduce una nota entre 0 y 20')
        nota = float(input('Introduce la nota: '))
        
    materia = input('Introduce la materia: ')

print(materias)
max_materia = max(materias, key=materias.get)
min_materia = min(materias, key=materias.get)
suma_materias = sum(materias.values())
promedio = suma_materias / len(materias)
print(f'La nota maxima de la materia {max_materia} es {materias.get(max_materia)}')
print(f'La nota minima de la materia {min_materia} es {materias.get(min_materia)}')
print(f'El promedio de las notas es {promedio:.2f}')
if promedio > 12:
    print(f'El alumno {nombre_alumno} ha aprobado el semestre')
else:
    print(f'El alumno {nombre_alumno} ha reprobado el semestre')
