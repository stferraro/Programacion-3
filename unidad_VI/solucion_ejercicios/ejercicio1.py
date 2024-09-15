vehiculos = {'moto': 1.50, 'carro': 3, 'camioneta': 6}
tipo_vehiculo = {'moto': 0, 'carro': 0, 'camioneta': 0}
dinero_vehiculo = {'moto': 0, 'carro': 0, 'camioneta': 0}
vehiculo = int (input('Introduce el tipo de vehiculo(0,1,2,3, 0 para terminar):  '))

while vehiculo != 0:
    
    while vehiculo < 0 or vehiculo > 3:
        print('Vehiculo no valido')
        vehiculo = int (input('Introduce el tipo de vehiculo(0,1,2,3, 0 para terminar):  '))
    
    if vehiculo == 1:
        tipo_vehiculo['moto'] = tipo_vehiculo.get('moto') + 1
        dinero_vehiculo['moto'] = dinero_vehiculo.get('moto') + vehiculos.get('moto') 
        print(str(vehiculos.get('moto')) + ' $')
    elif vehiculo == 2:
        tipo_vehiculo['carro'] = tipo_vehiculo.get('carro') + 1
        dinero_vehiculo['carro'] = dinero_vehiculo.get('carro') + vehiculos.get('carro') 
        print(str(vehiculos.get('carro')) + ' $')
        
    elif vehiculo == 3:
        tipo_vehiculo['camioneta'] = tipo_vehiculo.get('camioneta') + 1
        dinero_vehiculo['camioneta'] = dinero_vehiculo.get('camioneta') + vehiculos.get('camioneta')
        print(str(vehiculos.get('camioneta')) + ' $')
    else:
        print('Vehiculo no valido')
        
    vehiculo = int (input('Introduce el tipo de vehiculo(0,1,2,3, 0 para terminar):  '))
    
else:
    lista_valores_vehiculos = tipo_vehiculo.values()
    lista_recaudado = list(dinero_vehiculo.values())
    maximo_vehiculos = max(lista_valores_vehiculos)
    vehiculo_max = max(tipo_vehiculo, key=tipo_vehiculo.get)
    print('total recaudado por los vehiculos ' + str(sum(lista_recaudado)) + ' $')
    print('Total recaudado por las motos ' + str(dinero_vehiculo.get('moto')) + ' $')
    print('Total recaudado por los carros ' + str(dinero_vehiculo.get('carro')) + ' $')
    print('Total recaudado por las camionetas ' + str(dinero_vehiculo.get('camioneta')) + ' $')
    print('el vehiculo que mas pasa por el peaje es: ' + str(vehiculo_max))
    
    
    
    
    
    
    