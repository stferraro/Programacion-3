import random

def datos_personales():
    nombre = input("Por favor, ingresa tu nombre: ")
    print("Hola", nombre, "!")
    print("Vamos a jugar a Cho-Han!")
    return nombre

def jugada():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    jugada = dado1 + dado2
    if jugada % 2 == 0:
        jugada = 'Cho'
    else:
        jugada = 'Han'
    return jugada

def pide_jugada():
    jugada = input("Ingresa tu jugada Cho-Han: ")
    while jugada != 'Cho' and jugada != 'Han':
        print("Por favor, ingresa 'Cho' o 'Han'")
        jugada = input("Ingresa tu jugada Cho-Han: ")
    return jugada

def pide_saldo(saldo_inicial):
    saldo_jugar = float(input('Ingresa el saldo que deseas jugar: '))
    while saldo_jugar > saldo_inicial or saldo_jugar < 0:
        print("Por favor, ingresa un saldo entre 0 y", saldo_inicial)
        saldo_jugar = float(input("Ingresa el saldo que deseas jugar: "))
    return saldo_jugar

def run():
    nombre = datos_personales()
    saldo_inicial = 10
    partidos = {'ganados' : 0, 'perdidos' : 0}

    while True and saldo_inicial > 0:
        decision = input("Deseas jugar (s/n): ")
        jugada_comp = jugada()
        saldo_jugar = pide_saldo(saldo_inicial)
        jugada_user = pide_jugada()
        if jugada_user == jugada_comp:
            saldo_inicial += saldo_jugar
            partidos['ganados'] += 1
        else:
            saldo_inicial -= saldo_jugar
            partidos['perdidos'] += 1
        print("Tu saldo actual es:", saldo_inicial)
        if saldo_inicial == 0:
            print(f"Perdiste el juego {nombre} , te quedaste sin saldo")
            print("Partidos jugados:", partidos)
            break
        if decision == 'n':
            print("Gracias por jugar")
            print("Partidos Jugados:", partidos)
            break
        

if __name__ == '__main__':
    run()
        
    