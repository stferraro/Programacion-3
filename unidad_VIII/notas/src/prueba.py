from estudiante import Estudiante
from materia import Materia
import pandas as pd
import matplotlib.pyplot as plt


nombreEstudiante = input("Ingresa el nombre del estudiante: ")
apellidoEstudiante = input("Ingresa el apellido del estudiante: ")
cedulaEstudiante = input("Ingresa el cedula del estudiante: ")
sexoEstudiante = input("Ingresa el sexo del estudiante: ")
codigoEstudiante = input("Ingresa el codigo del estudiante: ")

materias = []

estudiante = Estudiante(
    nombreEstudiante,
    apellidoEstudiante,
    cedulaEstudiante,
    sexoEstudiante,
    codigoEstudiante,
    materias
)

nombre_materia = input("Ingresa la materia: ")
while nombre_materia != 'Fin':
    
    codigo = input("Ingresa el codigo de la materia: ")
    nota = float(input("Ingresa la nota: "))
    credito = int(input("Ingresa los creditos: "))
    materia = {
        
        "codigo": codigo,
        "nombre": nombre_materia,
        "nota": nota,
        "credito": credito
        
    }
    
    materias.append(materia)
    nombre_materia = input("Ingresa la materia: ")
    


df = pd.DataFrame(materias)
    

print(df)


df.to_csv("materias.csv", index=False)
df.to_excel("materias.xlsx", index=False)


promedio = df["nota"].mean()
print(f"El promedio de las notas es: {promedio:.2f}")

promedio_ponderado = (df["nota"] * df["credito"]).sum() / df["credito"].sum()
print(f"El promedio ponderado de las notas es: {promedio_ponderado:.2f}")

materias_aprobadas = df[df["nota"] >= 10]
print(materias_aprobadas)

materias_reprobadas = df[df["nota"] < 10]
print(materias_reprobadas)

plt.bar(df['nombre'], df['nota'], color='skyblue')
plt.xlabel('Materia')
plt.ylabel('Nota')
plt.title('Notas por Materia')
plt.show()

estadisticas_notas = df['nota'].describe()
print("Estadísticas de las notas:")
print(estadisticas_notas)
