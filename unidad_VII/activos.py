def valor_ano(ano):
    if ano >= 2012 and ano <= 2015:
        return 50
    elif ano >= 2016 and ano <= 2020:
        return 100
    elif ano >= 2021 and ano <= 2024:
        return 200
    return 0

def valor_categoria(categoria):
    if categoria == 'computadora':
        return 200
    elif categoria == 'impresora':
        return 150
    elif categoria == 'laptop':
        return 300
    return 0

def total(*valores):
    return sum(valores)

def run():
    activos = {}
    codigo = input('Codigo activo: ')
    while codigo != 'fin':
        ano = int(input('Año fabricacion: '))
        while ano < 0 or ano > 2024:
            print('Por favor, ingresa un año valido')
            ano = int(input('Año fabricacion: '))

        categoria = input('Categoria: ')
        while categoria not in ['computadora', 'impresora', 'laptop']:
            print('Por favor, ingresa una categoria valida')
            categoria = input('Categoria: ')
        
        valor1 = valor_ano(ano)
        valor2 = valor_categoria(categoria)
        valor = total(valor1, valor2)
        activos[codigo] = valor
        codigo = input('Codigo activo: ')
        
    print(activos)

run()