def areaTriangulo (base, altura):
    return (base * altura) / 2

def perimetroTriangulo (lado1, lado2, base):
    return (lado1 + lado2 + base)

lado1 = float(input("Ingresa el primer lado: "))
lado2 = float(input("Ingresa el segundo lado: "))
base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))

area = areaTriangulo(lado1, lado2)
perimetro = perimetroTriangulo(lado1, lado2, base)

print("El area es: ", area)
print("El perimetro es: ", perimetro)