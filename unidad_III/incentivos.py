salario = float(input('Introduce tu salario:  '))
meta_alcanzada = float(input('Introduce tu meta alcanzada:  '))

incentivo = 0

if meta_alcanzada >= 120:
    
    incentivo = 25 / 100
    salario = salario + (salario * incentivo)
    
elif 100 <= meta_alcanzada < 120:
    
    incentivo = 15 / 100
    salario = salario + (salario * incentivo)
       
elif  80 <= meta_alcanzada < 100:
    
    incentivo = 55 / 100
    salario = salario + (salario * incentivo)
    
else :
    
    incentivo = 0
    salario = salario - (salario * 0.10)
    
print(f'El nuevo salario es: {salario:.2f}')
    
    