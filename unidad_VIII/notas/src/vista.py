import tkinter as tk
from tkinter import messagebox

class Vista(tk.Tk):
    
    def __init__(self, root):
        
        self.root = root
        self.root.title('---Sistema de Notas---')
        self.root.geometry('700x700')
        
        self.crea_menu()
        self.crea_panel_estudiante()
        
    def crea_menu(self):
        menu = tk.Menu(self.root, borderwidth=1, tearoff=0)
        self.root.config(menu=menu)
        
        # File menu
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_cascade(label="Nuevo estudiante")
        file_menu.add_cascade(label="Nueva materia")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        
        # Help menu
        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        
    def exit_app(self):
        self.root.destroy()
        
    def show_about(self):
        messagebox.showinfo('Sistema de gestión de notas', 'Este sistema permite gestionar las notas de un estudiante por materia.')
        
        
    def crea_panel_estudiante(self):
        self.frame_estudiante = tk.Frame(self.root, padx=10, pady=10, bd=2, relief=tk.SOLID)
        self.frame_estudiante.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Título del panel
        self.label_titulo = tk.Label(self.frame_estudiante, text="Datos del Estudiante", font=("Arial", 16))
        self.label_titulo.grid(row=0, column=0, columnspan=4, pady=5)

        # Campos de entrada para los datos del estudiante
        # Primera fila: Nombre, Apellido, Cédula
        self.label_nombre = tk.Label(self.frame_estudiante, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, sticky=tk.E, padx=(5, 2), pady=5)
        self.entry_nombre = tk.Entry(self.frame_estudiante, width=20)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        self.label_apellido = tk.Label(self.frame_estudiante, text="Apellido:")
        self.label_apellido.grid(row=1, column=2, sticky=tk.E, padx=(5, 2), pady=5)
        self.entry_apellido = tk.Entry(self.frame_estudiante, width=20)
        self.entry_apellido.grid(row=1, column=3, padx=5, pady=5)

        # Segunda fila: Cédula, Sexo, Código
        self.label_cedula = tk.Label(self.frame_estudiante, text="Cédula:")
        self.label_cedula.grid(row=2, column=0, sticky=tk.E, padx=(5, 2), pady=5)
        self.entry_cedula = tk.Entry(self.frame_estudiante, width=20)
        self.entry_cedula.grid(row=2, column=1, padx=5, pady=5)

        self.label_sexo = tk.Label(self.frame_estudiante, text="Sexo:")
        self.label_sexo.grid(row=2, column=2, sticky=tk.E, padx=(5, 2), pady=5)
        self.entry_sexo = tk.Entry(self.frame_estudiante, width=3)
        self.entry_sexo.grid(row=2, column=3, padx=5, pady=5)

        self.label_codigo = tk.Label(self.frame_estudiante, text="Código:")
        self.label_codigo.grid(row=2, column=4, sticky=tk.E, padx=(5, 2), pady=5)
        self.entry_codigo = tk.Entry(self.frame_estudiante, width=20)
        self.entry_codigo.grid(row=2, column=5, padx=5, pady=5)

        # Botón para crear al estudiante en la tercera fila
        self.boton_crear = tk.Button(self.frame_estudiante, text="Crear Estudiante", command=self.crear_estudiante)
        self.boton_crear.grid(row=3, column=0, columnspan=6, pady=10)

    def crear_estudiante(self):
        pass
            
        
            
if __name__ == '__main__':
    root = tk.Tk()
    app = Vista(root)
    root.mainloop()