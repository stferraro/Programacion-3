def pedir_datos():
    nombre = input("Por favor ingresa tu nombre: ")
    apellido = input("Por favor ingresa tu apellido: ")
    cedula = input("Por favor ingresa tu cedula: ")
    return nombre, apellido, cedula

def confirmar_compra():
    decision = input("¿Deseas realizar la compra? (s/n): ")
    while decision != 's' and decision != 'n':
        print("Por favor, ingresa 's' o 'n'")
        decision = input("¿Deseas realizar la compra? (s/n): ")
    return decision

def compra_acciones(acciones):
    nombre_accion = input('Codigo Accion: ')
    
    precio = float(input('Precio: '))
    while precio <= 0:
        print("Por favor, ingresa un precio positivo")
        precio = float(input('Precio: '))
        
    acciones[nombre_accion] = precio
    return acciones

def imprimir_acciones(acciones):
    for accion,precio in acciones.items():
        print(f"{accion}: {precio}")
    
def total_pago(acciones):
    return sum(acciones.values())

def run():
    nombre, apellido, cedula = pedir_datos()
    decision = confirmar_compra()
    acciones = {}
    while decision == 's':
        compra_acciones(acciones)
        decision = confirmar_compra()
    imprimir_acciones(acciones)
    print(f"El total a pagar por el Sr. {nombre} {apellido} con cedula {cedula} es: {total_pago(acciones)}")
    
    
run()