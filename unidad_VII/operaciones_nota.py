def agrega_materias():
    materias = {}
    materia = input("Ingresa una materia: ")
    while materia != 'Fin':
        nota = float(input("Ingresa la nota: "))
        nota = valida_nota(nota)
            
        credito = int(input("Ingresa los creditos: "))
        credito = valida_creditos(credito)
        
        materias[materia] = {'nota': nota, 'credito': credito}
        materia = input("Ingresa una materia: ")

    return materias
        
def valida_nota (nota):
    while nota < 0 or nota > 20:
        print("Por favor, ingresa una nota entre 0 y 20")
        nota = float(input("Ingresa la nota: "))
    return nota

def valida_creditos (creditos):
    while creditos < 0:
        print("Por favor, ingresa un valor positivo")
        creditos = int(input("Ingresa los creditos: "))
    return creditos

def promedio (materias):
    total_creditos = 0
    total_notas = 0
    for clave, datos in materias.items():
        total_creditos += datos['credito']
        total_notas += datos['nota'] * datos['credito']
    promedio = total_notas / total_creditos
    return promedio

def verifica_promedio (promedio):
    if promedio >= 12:
        print("¡Felicidades, has aprobado el semestre!")
    else:
        print("Lo siento, no has aprobado el semestre.")
    
if __name__ == "__main__":
    materias = agrega_materias()
    promedio = promedio(materias)
    pasaste = verifica_promedio(promedio)
    print(f"Tu promedio es: {promedio:.2f}")
    print(materias)