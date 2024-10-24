import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from convertidor import Convertidor

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Currency Converter")
        self.geometry("400x300")

        # Create menu
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Convert to Dollars", command=self.convert_to_dollars)
        file_menu.add_command(label="Convert to Euros", command=self.convert_to_euros)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # About menu
        about_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="Converter", command=self.show_about)

        # Labels and Entry
        self.label_bs = tk.Label(self, text="Enter amount in Bolivares:")
        self.label_bs.pack(pady=10)

        self.entry_bs = tk.Entry(self)
        self.entry_bs.pack(pady=5)

        self.label_result = tk.Label(self, text="Result:")
        self.label_result.pack(pady=10)

        self.result_var = tk.StringVar()
        self.result_label = tk.Label(self, textvariable=self.result_var)
        self.result_label.pack(pady=5)

        # Buttons
        self.convert_dollars_button = tk.Button(self, text="Convert to Dollars", command=self.convert_to_dollars)
        self.convert_dollars_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.convert_euros_button = tk.Button(self, text="Convert to Euros", command=self.convert_to_euros)
        self.convert_euros_button.pack(side=tk.RIGHT, padx=20, pady=20)

    def show_about(self):
        # Show an about message box
        messagebox.showinfo("About Converter", 
                            "This application converts Bolivares to Dollars and Euros.\n"
                            "Input the amount in Bolivares and click to convert.")

    def convert_to_dollars(self):
        self.convert_currency('dollars')

    def convert_to_euros(self):
        self.convert_currency('euros')

    def convert_currency(self, currency):
        try:
            cantidad_bs = float(self.entry_bs.get())
            convertidor = Convertidor(cantidad_bs)

            if currency == 'dollars':
                result = convertidor.convertir_bs_a_dolares()
                self.result_var.set(f"{result:.4f} Dollars")
            else:
                result = convertidor.convertir_bs_a_euros()
                self.result_var.set(f"{result:.4f} Euros")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
