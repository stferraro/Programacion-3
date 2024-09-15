empleados = {}
continua = 's'

while continua == 's':
    
    print('Introduce el nombre del empleado')
    nombre = input('Nombre: ')
    salario = float(input('Salario: '))
    
    empleados[nombre] = salario
    continua = input('¿Deseas introducir otro empleado? (s/n): ')
    
    while continua != 's' and continua != 'n':
        print('Introduce s o n')
        continua = input('¿Deseas introducir otro empleado? (s/n): ')
        
print(empleados)
max_sueldo = max(empleados, key=empleados.get)
min_sueldo = min(empleados, key=empleados.get)
print(f'El sueldo mas alto es {max(empleados.values())} $ - {max_sueldo}')
print(f'El sueldo mas bajo es {min(empleados.values())} $ - {min_sueldo}')
print(f'El promedio de las sueldos es {sum(empleados.values()) / len(empleados):.2f} $')
contador_1000 = 0
contador_men_1000 = 0
for i in empleados.values():
    if i > 1000:
        contador_1000 += 1
    else:
        contador_men_1000 += 1
print(f'Hay {contador_1000} empleados con mas de 1000 $')
print(f'Hay {contador_men_1000} empleados con menos de 1000 $')
