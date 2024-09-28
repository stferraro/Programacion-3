def pedir_datos():
    nombre = input("Por favor ingresa tu nombre: ")
    apellido = input("Por favor ingresa tu apellido: ")
    cedula = input("Por favor ingresa tu cedula: ")
    return nombre, apellido, cedula

def determina_sueldo(cargo):
    sueldo = 0
    match cargo:
        case "Gerente":
            sueldo = 3000
        case "Supervisor":
            sueldo= 2000
        case "Empleado":
            sueldo = 1500
        case _:
            sueldo = 0
    return sueldo

def bono_edad (sueldo, edad):
    bono = 0
    if edad > 25 and edad < 35:
        bono = sueldo * 0.1
    elif edad >= 35 and edad < 45:
        bono = sueldo * 0.15
    elif edad >= 45 and edad < 65:
        bono = sueldo * 0.25
    else:
        bono = 0
    return bono

def bono_hijos (sueldo, num_hijos):
    bono = 0
    if num_hijos > 3:
        bono = sueldo * 0.20 * num_hijos
    elif num_hijos <= 3 and num_hijos >= 1:
        bono = sueldo * 0.10 * num_hijos
    else:
        bono = 0
    return bono

def total_sueldo(*valores):
    return sum (valores)

def run ():
    nombre, apellido, cedula = pedir_datos()
    cargo = input("Por favor ingresa tu cargo: ")
    sueldo = determina_sueldo(cargo)
    edad = int(input("Por favor ingresa tu edad: "))
    bonoEdad = bono_edad(sueldo, edad)
    num_hijos = int(input("Por favor ingresa el numero de hijos: "))
    bonoHijos = bono_hijos(sueldo, num_hijos)
    total = total_sueldo(sueldo, bonoEdad, bonoHijos)
    print(f'El sueldo total de {nombre} {apellido} con cedula {cedula} es: {total:.2f} $$')

if __name__ == "__main__":
    run()

    