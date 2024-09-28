def pide_datos():
    nombre = input('Introduce tu nombre: ')
    apellido = input('Introduce tu apellido: ')
    cedula = input('Introduce tu cedula: ')

    return nombre, apellido, cedula

def agrega_vehiculos(vehiculos, tipo_vehiculo):
    vehiculos[tipo_vehiculo] = vehiculos.get(tipo_vehiculo, 0) + 1
    return vehiculos

def calcula_tarifa(vehiculo):
    tarifa = 0
    if vehiculo == 'moto':
        tarifa = 3.50
    elif vehiculo == 'carro':
        tarifa = 12
    elif vehiculo == 'camion':
        tarifa = 16
    return tarifa

def calcula_dinero(tarifa, vehiculos, tipo_vehiculos):
    vehiculos[tipo_vehiculos] += tarifa
    return vehiculos

def calcula_vehiculo_max(vehiculos):
    lista_valores_vehiculos = list(vehiculos.values())
    maximo_vehiculos = max(lista_valores_vehiculos)
    vehiculo_max = max(vehiculos, key=vehiculos.get)
    return vehiculo_max, maximo_vehiculos

def total_recaudado(vehiculos):
    return sum(vehiculos.values())

def calcula_vehiculos(vehiculos):
    if 'moto' in vehiculos:
        vehiculos['moto'] = vehiculos['moto'] + 1
    elif 'carro' in vehiculos:
        vehiculos['carro'] = vehiculos['carro'] + 1
    elif 'camion' in vehiculos:
        vehiculos['camion'] = vehiculos['camion'] + 1
    return vehiculos
def verifica_input():
    seguir = input('¿Quieres seguir agregando vehiculos? (s/n): ')
    while seguir != 's' and seguir != 'n':
        print('Introduce s o n')
        seguir = input('¿Quieres seguir agregando vehiculos? (s/n): ')
    return seguir

def run():
    nombre, apellido, cedula = pide_datos()
    print('Bienvenido ' + nombre + ' ' + apellido + ' con cedula ' + cedula)
    print('Vamos a registrar el peaje de hoy')
    vehiculos = {'moto': 0, 'carro': 0, 'camion': 0}
    costos = {'moto': 0, 'carro': 0, 'camion': 0}
    while True:
        vehiculo = input('Introduce el tipo de vehiculo (moto, carro, camion): ')
        agrega_vehiculos(vehiculos, vehiculo)
        tarifa = calcula_tarifa(vehiculo)
        print('La tarifa del ' + vehiculo + ' es de ' + str(tarifa) + ' $')
        costos = calcula_dinero(tarifa, costos, vehiculo)
        seguir = verifica_input()
        
        if seguir == 'n':
            vehiculo_max, maximo_vehiculos = calcula_vehiculo_max(vehiculos)
            print('El vehiculo que mas pasa por el peaje es: ' + vehiculo_max + ' y han pasado ' + str(maximo_vehiculos) + ' vehiculos')
            print('El total recaudado es de: ' + str(total_recaudado(costos)))
            
            break
    
run()
    
        