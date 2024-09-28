import random

def obtener_combinacion(colors = []):
    return random.sample(colors, len(colors))

def verificar_combinacion(combinacion_ganadora, combinacion_jugador):
    correctos = sum([combinacion_ganadora[i] == combinacion_jugador[i] for i in range(4)])
    return correctos

def jugar():
    nombre = input("Por favor ingresa tu nombre: ")
    apellido = input("Por favor ingresa tu apellido: ")
    print(f"Bienvenido {nombre} {apellido}!")
    colores = ['rojo', 'verde', 'amarillo', 'azul']

    saldo_inicial = float(input("Ingresa tu saldo inicial: "))
    saldo_actual = saldo_inicial
    combinacion_ganadora = obtener_combinacion(colores)

    while True:

        print("La combinación ganadora tiene 4 colores. ¡Intenta adivinarla!")
        print(f"Saldo inicial: {saldo_inicial}, Saldo actual: {saldo_actual}")

        # Ingresar la apuesta
        apuesta = float(input(f"Ingrese la cantidad a apostar (saldo actual: {saldo_actual}): "))
        
        if apuesta > saldo_actual:
            print("La cantidad apostada no puede ser mayor que el saldo actual. Intenta de nuevo.")
            continue

        # Elegir los colores
        colores = ['rojo', 'verde', 'amarillo', 'azul']
        combinacion_jugador = []
        for i in range(4):
            color = input(f"Ingresa el color (opciones: {colores}): ")
            while color not in colores:
                print("Color inválido. Intenta de nuevo.")
                color = input(f"Ingresa el color (opciones: {colores}): ")
            combinacion_jugador.append(color)

        # Verificar cuántos colores están correctos y en la posición correcta
        correctos = verificar_combinacion(combinacion_ganadora, combinacion_jugador)
        print(f"Número de colores coincidentes en los índices correctos: {correctos}")

        if correctos == 4:
            saldo_actual += apuesta
            print(f"¡Ganaste! Tu saldo final es: {saldo_actual}")
            break  # Terminar el juego si adivinó correctamente
        else:
            saldo_actual -= apuesta
            print(f"No acertaste. Tu saldo actual es: {saldo_actual}")

            # Verificar si el saldo se agotó
            if saldo_actual <= 0:
                print("Te has quedado sin saldo. ¡Juego terminado!")
                break

            # Preguntar si desea seguir jugando
            continuar = input("¿Quieres seguir jugando? (s/n): ").lower()
            if continuar == 'n':
                print(f"Gracias por jugar. Tu saldo final es: {saldo_actual}")
                print(f"La combinación ganadora fue: {combinacion_ganadora}")
                break

# Ejecutar el juego
jugar()







