def areaCuadrado (base, altura):
    return base * altura

def perimetroCuadrado (base, altura):
    return 2 * (base + altura)


base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))

area = areaCuadrado(base, altura)
perimetro = perimetroCuadrado(base, altura)

print("El area es: ", area)
print("El perimetro es: ", perimetro)