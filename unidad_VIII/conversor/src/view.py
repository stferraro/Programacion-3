from convertidor import Convertidor

cantidad_bs = float(input('Ingresa la cantidad de dinero en Bolivares: '))          

opcion = float(input('Ingresa la opción deseada: \n-1. Convertir a Dólares \n-2. Convertir a Euros \n-0. Salir: '))
while opcion < 0 or opcion > 2:
    print('Por favor, ingresa una opción válida')
    opcion = float(input('Ingresa la opción deseada: \n1. Convertir a Dólares \n2. Convertir a Euros \n0. Salir:'))
    
while True:
    if opcion == 1:
        
        print('Vas a cambiar de Bs a Euros')
        convertidor = Convertidor(cantidad_bs)
        print(f'{convertidor.convertir_bs_a_dolares():.4f} Dólares')
        opcion = float(input('Ingresa la opción deseada: \n-1. Convertir a Dólares \n-2. Convertir a Euros \n-0. Salir: '))
        
    elif opcion == 2:
        
        print('Vas a cambiar de Bs a Euros')
        convertidor = Convertidor(cantidad_bs)
        print(f'{convertidor.convertir_bs_a_euros():.4f} Euros')
        opcion = float(input('Ingresa la opción deseada: \n-1. Convertir a Dólares \n-2. Convertir a Euros \n-0. Salir: '))
        
    elif opcion == 0:
        break
    
    