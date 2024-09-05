a = float(input('Introduce el valor de a:  '))
b = float(input('Introduce el valor de b:  '))
c = float(input('Introduce el valor de c:  '))


if (a + b) > c and (a + c) > b and (b + c) > a: 
    print('Es un triangulo')
    
    if a == b == c:
        print('Es equilatero')
    elif a == b or a == c or b == c:
        print('Es isosceles')
    else:
        print('Es escaleno')
else:
    print('No es un triangulo')