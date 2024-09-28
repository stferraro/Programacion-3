import random

def solicita_datos():
    nombre = input("Por favor ingresa tu nombre: ")
    apellido = input("Por favor ingresa tu apellido: ")
    cedula = input("Por favor ingresa tu cedula: ")
    return nombre, apellido, cedula

def agrega_numeros():
    numeros = []
    for i in range(6):
        numero = int(input("Por favor ingresa un numero: "))
        numeros.append(numero)
    return numeros

def ingresa_saldo():
    saldo = float(input("Por favor ingresa tu saldo: "))
    return saldo

def numero_seleccionado(numeros=[]):
    numero_seleccionado = random.choice(numeros)
    return numero_seleccionado

def calcula_ganancia(saldo, numero_seleccionado):
    intentos = 0
    while intentos < 3:  
        numero_usuario = int(input(f"Intento {intentos + 1}: Por favor, ingresa un número de la lista {numeros}: "))
        intentos += 1

        if numero_usuario == numero_seleccionado:
            if intentos == 1:
                saldo += saldo  
                print("¡Felicidades! Adivinaste al primer intento. Ganaste el 100% de tu saldo.")
            elif intentos == 2:
                saldo += (saldo * 50) / 100  
                print("¡Felicidades! Adivinaste al segundo intento. Ganaste el 50% de tu saldo.")
            elif intentos == 3:
                saldo += (saldo * 33.33) / 100  
                print("¡Felicidades! Adivinaste al tercer intento. Ganaste el 33.33% de tu saldo.")
            break
        else:
            print("Tu número es incorrecto.")
    
    if intentos == 3 and numero_usuario != numero_seleccionado:
        print(f"Lo siento, no adivinaste. El número correcto era {numero_seleccionado}. Pierdes todo tu saldo.")
        saldo = 0  # Se le quita el saldo total

    return saldo

if __name__ == "__main__":
    nombre, apellido, cedula = solicita_datos()
    numeros = agrega_numeros()
    saldo = ingresa_saldo()
    numero_seleccionado = numero_seleccionado(numeros)
    saldo = calcula_ganancia(saldo, numero_seleccionado)
    print("Hola", nombre, apellido, "tu cedula es", cedula, "y tus numeros son", numeros, "tu saldo es", saldo)