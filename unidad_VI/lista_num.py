lista_a = []

for i in range(5):

    numero = float(input('Introduce un numero: '))
    lista_a.append(numero)

num_max = max(lista_a)
num_min = min(lista_a)
suma_lista = sum(lista_a)

contador_1000 = 0

for i in lista_a:
    if i > 1000:
        contador_1000 += 1

lista_a.sort(reverse=True)
b = tuple(lista_a)
print(lista_a)
print(b)
print(f'''-La suma de los elementos de la lista es: {suma_lista:.2f}
    -El numero mas alto es: {num_max:.2f}
    -El numero mas bajo es: {num_min:.2f}''')
