productos = {}

print('Bienvenido al supermercado')

respuesta = 's'

while respuesta == 's':
    print('Introduce el nombre del producto')
    nombre = input('Producto: ')
    print('Introduce el precio del producto')
    precio = float(input('Precio: '))
    productos[nombre] = precio
    print('¿Deseas introducir otro producto?')
    respuesta = input('s/n: ')

print(productos)

#calculo de la suma de los precios
suma = 0
for precio in productos.values():
    suma += precio

print(f'La suma total de los productos es: {suma:.2f}')


if suma > 100:
    descuento = suma * 0.1
    total = suma - descuento
    print(f'El total a pagar es: {total:.2f}')

#calculo del producto mas barato
minimo = float('inf')
lista_precios = list(productos.values())
for i in lista_precios:
    if i < minimo:
        minimo = i

producto_min = list(productos.keys())[list(productos.values()).index(minimo)]
print(f'El producto mas barato es: {producto_min}')