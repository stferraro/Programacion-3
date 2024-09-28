def descuento(costo, porcentaje):
    return costo - (costo * porcentaje) / 100

def aplicar_iva(costo, porcentaje):
    return costo + (costo * porcentaje) / 100

costo = float(input("Ingresa el costo: "))
porcentaje = float(input("Ingresa el porcentaje de descuento: "))
costo_descuento = descuento(costo, porcentaje)
costo_iva = aplicar_iva(costo, porcentaje)
print(f"El valor con descuento es: {costo_descuento:.2f}")
print(f"El valor con IVA es: {costo_iva:.2f}")