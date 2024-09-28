productos = {}

producto = input('Producto: ')

while producto != 'n':

    precio = float(input('Precio: '))
    while precio < 0:
        print('Debes introducir un valor positivo')
        precio = float(input('Precio: '))

    productos[producto] = precio

    producto = input('Producto: ')

else:
    print(productos)
    producto_max = max(productos, key=productos.get)
    print(f'El producto mas caro es: {producto_max} - y su valor es de: {productos.get(producto_max):.2f}')
    producto_min = min(productos, key=productos.get)
    print(f'El producto mas caro es: {producto_min} - y su valor es de: {productos.get(producto_min):.2f}')
    print(f'El valor de todos los productos registrados es de: {sum(productos.values():.2f)}')
