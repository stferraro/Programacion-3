import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import os

class JuegoPPT(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Piedra, Papel o Tijera")
        
        # Obtener la ruta a la carpeta de recursos
        self.ruta_recursos = os.path.join(os.path.dirname(__file__), 'recursos')

        # Verificar la existencia de las imágenes
        print("Ruta de recursos:", self.ruta_recursos)
        print("Archivos en recursos:", os.listdir(self.ruta_recursos))

        # Cargar las imágenes
        self.imagenes = {
            'piedra': ImageTk.PhotoImage(file=os.path.join(self.ruta_recursos, 'sasso1.gif')),
            'papel': ImageTk.PhotoImage(file=os.path.join(self.ruta_recursos, 'carta1.gif')),
            'tijera': ImageTk.PhotoImage(file=os.path.join(self.ruta_recursos, 'forbici1.gif'))
        }

        # Crear los widgets
        self.label = tk.Label(self, text="Elige una opción:")
        self.label.pack(pady=10)

        self.frame_imagenes = tk.Frame(self)
        self.frame_imagenes.pack()

        self.boton_piedra = tk.Button(self.frame_imagenes, image=self.imagenes['piedra'], command=lambda: self.elegir_opcion('piedra'))
        self.boton_piedra.grid(row=0, column=0, padx=10)

        self.boton_papel = tk.Button(self.frame_imagenes, image=self.imagenes['papel'], command=lambda: self.elegir_opcion('papel'))
        self.boton_papel.grid(row=0, column=1, padx=10)

        self.boton_tijera = tk.Button(self.frame_imagenes, image=self.imagenes['tijera'], command=lambda: self.elegir_opcion('tijera'))
        self.boton_tijera.grid(row=0, column=2, padx=10)

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.pack(pady=10)

        self.opciones = ['piedra', 'papel', 'tijera']

        # Contadores de partidos ganados
        self.ganados_jugador = 0
        self.ganados_maquina = 0

    def elegir_opcion(self, opcion_usuario):
        opcion_maquina = random.choice(self.opciones)

        # Mostrar la elección de la máquina
        self.label_resultado.config(text=f"Elegiste {opcion_usuario}. La máquina eligió {opcion_maquina}.")

        # Determinar el resultado
        if opcion_usuario == opcion_maquina:
            resultado = "Empate"
        elif (opcion_usuario == 'piedra' and opcion_maquina == 'tijera') or \
             (opcion_usuario == 'papel' and opcion_maquina == 'piedra') or \
             (opcion_usuario == 'tijera' and opcion_maquina == 'papel'):
            resultado = "¡Ganaste!"
            self.ganados_jugador += 1
        else:
            resultado = "¡Perdiste!"
            self.ganados_maquina += 1

        self.label_resultado.config(text=f"{resultado}")

    def salir_del_juego(self):
        mensaje = f"Total de partidos ganados por ti: {self.ganados_jugador}\n"
        mensaje += f"Total de partidos ganados por la computadora: {self.ganados_maquina}"

        tk.messagebox.showinfo("Estadísticas de juego", mensaje)
        self.destroy()

if __name__ == "__main__":
    app = JuegoPPT()
    
    # Agregar un botón para salir del juego
    boton_salir = tk.Button(app, text="Salir del juego", command=app.salir_del_juego)
    boton_salir.pack(pady=20)

    app.mainloop()
