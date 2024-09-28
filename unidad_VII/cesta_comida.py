def descuento(costo, porcentaje):
    costo = costo - (costo * porcentaje) / 100
    return costo

def aplica_iva(costo, porcentaje):
    costo = costo  + (costo * porcentaje) / 100
    return costo

def costruye_cesta():
    cesta = {}
    decision = 's'
    while decision == 's':
        producto = input("Ingresa el nombre del articulo: ")
        precio = float(input("Ingresa el precio del articulo: "))
        while precio <= 0:
            print("Por favor, ingresa un precio positivo")
            precio = float(input("Ingresa el precio del articulo: "))
            
        cesta[producto] = precio
        decision = input("Deseas agregar otro articulo (s/n): ")
        
        if decision == 'n':
            break

    return cesta

def valor_cesta(cesta):
    valor = 0
    for i in cesta.values():
        valor = valor + i
    return valor

def valor_operaciones (cesta):
    valor = valor_cesta(cesta)
    iva = float(input("Ingresa el porcentaje de IVA: "))
    porcentaje_descuento = float(input("Ingresa el porcentaje de descuento: "))
    valor_descuento = descuento (valor, porcentaje_descuento)
    valor_iva = aplica_iva (valor, iva)
    return valor_iva, valor_descuento

def run():
    cesta = costruye_cesta()
    valor_iva, valor_descuento = valor_operaciones(cesta)
    print("La cesta es: ", cesta)
    print(f"El valor de la cesta es:  {valor_iva:.2f}")
    print(f"El valor con descuento es:  {valor_descuento:.2f}")

if __name__ == '__main__':
    run()
    
    

    
        