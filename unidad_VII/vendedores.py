def percentage_comission(amount):
    if amount > 0 and amount < 75000:
        return 5 * amount / 100
    elif amount >= 95000 and amount < 200000:
        return 7 * amount / 100
    elif amount >= 300000 and amount < 1000000:
        return 8 * amount / 100
    elif amount > 1500000:
        return 10 * amount / 100
    else:
        return 6 * amount / 100
    return 0

def bono_edad(sexo, edad):
    if sexo == 'M' and edad >= 55:
        return 40000
    elif sexo == 'H' and edad >= 60:
        return 40000
    return 0

def valida_sexo(sexo):
    while sexo != 'M' and sexo != 'H':
        sexo = input('Introduce M o H: ')
    return sexo

def valida_monto(valor):
    while valor < 0:
        valor = float(input('Usar valor positivo: '))
    return valor

def valida_edad(edad):
    while edad < 0 and edad >= 120:
        edad = float(input('edad: '))
    return edad

def total_salary (*valores):
    return sum(valores)

def personal_values():
    name= input('Nombre y apellido del Vendedor: ')
    sueldo = float(input('Sueldo base: '))
    return name, sueldo

def agrega_vendedor(vendedores):
    while True:
        nombre, sueldo = personal_values()
        amount = float(input('Monto Vendido: '))
        amount = valida_monto(amount)
        comission = percentage_comission(amount)
        sexo = input('Valida Sexo M/H: ')
        sexo = valida_sexo(sexo)
        edad = int(input('edad: '))
        edad = valida_edad(edad)
        bono = bono_edad(sexo, edad)
        total = total_salary(sueldo, comission, bono)
        vendedor = input('Desea seguir agregando vendedores(s/n): ')
        while vendedor != 's' and vendedor != 'n':
            vendedor = input('Desea seguir agregando vendedores(s/n): ')
        if vendedor == 'n':
            vendedores[nombre]= total
            print(vendedores)
            break
        else:
            vendedores[nombre]= total
            
agrega_vendedor(vendedores={})
            
    
    