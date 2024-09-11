import random

decision = 's'
opciones = ['piedra', 'papel', 'tijera']
partidos_ganados = {'computador': 0, 'jugador': 0}

print('Juguemos a Piedra, Papel o Tijera')
nombre_jugador = input('Introduce tu nombre: ')
print(f'Bienvenido {nombre_jugador} al juego')

while decision == 's':
    
    print('Piedra, papel o tijera?')
    eleccion = input('Tu elección: ')
    eleccion = eleccion.lower()
    
    while eleccion not in ['piedra', 'papel', 'tijera']:
        print('Piedra, papel o tijera?')
        eleccion = input('Tu elección: ')
        eleccion = eleccion.lower()
        
    computador = random.choice(opciones)
    
    if (eleccion == 'piedra' and computador == 'tijera') or (eleccion == 'papel' and computador == 'piedra') or (eleccion == 'tijera' and computador == 'papel'):
        partidos_ganados['jugador'] += 1
        print(f'{nombre_jugador} gana')
    elif (eleccion == 'piedra' and computador == 'papel') or (eleccion == 'papel' and computador == 'tijera') or (eleccion == 'tijera' and computador == 'piedra'):
        partidos_ganados['computador'] += 1
        print('La computadora gana')
    elif eleccion == computador:
        print('Empate')
    
    decision = input('¿Quieres jugar de nuevo? (s/n): ')
    
    if decision == 'n':
        print('Hasta la proxima')
        print(f'Partidos ganados por el jugador {nombre_jugador}: {partidos_ganados["jugador"]}')
        print(f'Partidos ganados por la computadora: {partidos_ganados["computador"]}')
        if partidos_ganados['jugador'] > partidos_ganados['computador']:
            print(f'{nombre_jugador} es el ganador')
        elif partidos_ganados['jugador'] < partidos_ganados['computador']:
            print('La computadora es el ganador')
        else:
            print('Empate')
        break
    
    while decision != 's' and decision != 'n':
        print('Por favor, introduce s para si o n para no')
        decision = input('¿Quieres jugar de nuevo? (s/n): ')
    
