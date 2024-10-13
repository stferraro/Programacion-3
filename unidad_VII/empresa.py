def pide_datos():
    nombre = input('Introduce tu nombre: ')
    apellido = input('Introduce tu apellido: ')
    cedula = input('Introduce tu cedula: ')

    return nombre, apellido, cedula

def calcula_sueldo(cargo):
    sueldo = 0
    match cargo:
        case "Gerente":
            sueldo = 3000
        case "Supervisor":
            sueldo = 2000
        case "Empleado":
            sueldo = 1500
    return sueldo

def bono_antiguedad(sueldo, antiguedad):
    bono = 0
    if antiguedad >= 1 and antiguedad <= 3:
        bono = sueldo * 0.10 * antiguedad
    elif antiguedad > 3:
        bono = sueldo * 0.20 * antiguedad
    else :
        bono = 0

    return bono

def bono_asistencia(dias, sueldo):
    if dias == 30:
        bono = sueldo * 0.20
    else:
        bono = 0
    return bono

def bono_hijos(sueldo, num_hijos):
    bono = 0
    if num_hijos > 2:
        bono = sueldo * 0.20 * num_hijos
    else:
        bono = 0
    return bono

def total_sueldo(*valores):
    return sum (valores)
def promedio_sueldos(sueldos):
    return sum(sueldos) / len(sueldos)

def calcula_utilidades(promedio):
    return (promedio / 365) * 120

def run():
    nombre, apellido, cedula = pide_datos()
    cargo = input("Por favor ingresa tu cargo: ")
    sueldo = calcula_sueldo(cargo)
    sueldos = []
    for i in range(3):
        antiguedad = int(input("Por favor ingresa la antiguedad: "))
        bonoAntiguedad = bono_antiguedad(sueldo, antiguedad)
        dias = int(input("Por favor ingresa los dias laborados: "))
        bonoAsistencia = bono_asistencia(dias, sueldo)
        num_hijos = int(input("Por favor ingresa el numero de hijos: "))
        bonoHijos = bono_hijos(sueldo, num_hijos)
        total = total_sueldo(bonoAntiguedad, bonoAsistencia, bonoHijos)
        print(f'El sueldo total de {nombre} {apellido} con cedula {cedula} del mes {i+1} es: {total:.2f} $$')
        sueldos.append(total)
    print(sueldos)

    promedio = promedio_sueldos(sueldos)
    sueldos_tot = sum(sueldos)
    utilidades = calcula_utilidades(promedio)
    
    print(f'El sueldo total de {nombre} {apellido} con cedula {cedula} es: {sueldos_tot:.2f} $$')
    print(f'Las utilidades de {nombre} {apellido} con cedula {cedula} es: {utilidades:.2f} $$') 
    
if __name__ == "__main__":
    run()
        

