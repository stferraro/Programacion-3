def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b

a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))

print("Suma: ", suma(a, b))
print("Resta: ", resta(a, b))
print("Multiplicacion: ", multiplicar(a, b))
print("Division: ", dividir(a, b))