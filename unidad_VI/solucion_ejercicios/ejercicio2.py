empleados = {}
continua = 's'

while continua == 's':
    
    print('Introduce el nombre del empleado')
    nombre = input('Nombre: ')
    print('Introduce el sueldo del empleado')
    print(1, 'Empleado', 2, 'Supervisor', 3, 'Gerente')
    cargo = int(input('Cargo: '))
    
    if cargo == 1:
        sueldo = 1000
        print('Empleado')
        print(f'Sueldo: {sueldo:.2f} $$')
    elif cargo == 2:
        sueldo = 2000
        print('Supervisor')
        print(f'Sueldo: {sueldo:.2f} $$')
    elif cargo == 3:
        sueldo = 5000
        print('Gerente')
        print(f'Sueldo: {sueldo:.2f} $$')
    else:
        cargo = int(input('Introduce el cargo correcto: '))
    empleados[nombre] = sueldo
    continua = input('¿Deseas introducir otro empleado? (s/n): ')
    
    while continua != 's' and continua != 'n':
        print('Introduce s o n')
        continua = input('¿Deseas introducir otro empleado? (s/n): ')
    
else:
    print(empleados)
    for nombre, sueldo in empleados.items():
        print(f'{nombre} {sueldo:.2f} $$')
    suma_sueldos = sum(empleados.values())
    print(f'La suma de sueldos es: {suma_sueldos:.2f} $$')
    
    


    