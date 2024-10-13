def esTriangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
    
def area(base, altura):
    return (base * altura) / 2

def perimetro(lado1, lado2, base):
    return (lado1 + lado2 + base)

def run():
    lado1 = float(input("Ingresa el primer lado: "))
    lado2 = float(input("Ingresa el segundo lado: "))
    base = float(input("Ingresa la base: "))
    
    if esTriangulo(lado1, lado2, base):
        altura = float(input("Ingresa la altura: "))
        print("El area es: ", area(base, altura))
        print("El perimetro es: ", perimetro(lado1, lado2, base))
    else:
        print("No es un triangulo")
        
run()