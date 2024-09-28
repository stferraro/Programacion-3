def agregar_numeros(lista, n):
    for i in range (n):
        num = int(input("Ingresa un numero: "))
        lista.append(num)
    return lista

def imprimir_lista(lista):
    print("Lista de numeros: ", lista)
    

numeros = []
n = int(input("Ingresa la cantidad de numeros que deseas agregar: "))
numeros = agregar_numeros(numeros, n)
imprimir_lista(numeros)