vehiculos = {'moto': 3.50, 'carro': 12, 'camion': 16}
cantidad_vehiculos = {'moto': 0, 'carro': 0, 'camion': 0}
cantidad_dinero = {'moto': 0, 'carro': 0, 'camion': 0}

vehiculo = int (input('Introduce el tipo de vehiculo(0,1,2,3, 0 para terminar):  '))

while vehiculo != 0:
    if vehiculo == 1:
        print(str(vehiculos.get('moto')) + ' $')
        cantidad_vehiculos['moto'] = cantidad_vehiculos['moto'] + 1
        cantidad_dinero['moto'] = cantidad_dinero['moto'] + vehiculos.get('moto')
    elif vehiculo == 2:
        print(str(vehiculos.get('carro')) + ' $')
        cantidad_vehiculos['carro'] = cantidad_vehiculos['carro'] + 1
        cantidad_dinero['carro'] = cantidad_dinero['carro'] + vehiculos.get('carro')
    elif vehiculo == 3:
        print(str(vehiculos.get('camion')) + ' $')
        cantidad_vehiculos['camion'] = cantidad_vehiculos['camion'] + 1
        cantidad_dinero['camion'] = cantidad_dinero['camion'] + vehiculos.get('camion')
    else:
        print('Vehiculo no valido')
        
    vehiculo = int (input('Introduce el tipo de vehiculo(0,1,2,3, 0 para terminar):  '))

print(cantidad_vehiculos)
lista_valores_vehiculos = cantidad_vehiculos.values()
maximo_vehiculos = max(lista_valores_vehiculos)
vehiculo_max = max(cantidad_vehiculos, key=cantidad_vehiculos.get)


print ('total recaudados por las motos ' + str(cantidad_dinero['moto']))
print ('total recaudados por los carros ' + str(cantidad_dinero['carro']))
print ('total recaudados por los camiones ' + str(cantidad_dinero['camion']))
print('el vehiculo que mas pasa por el peaje es: ' + str(vehiculo_max))
