"""
Este es un ejemplo simple, brindado en la documentación oficial de Python:
https://docs.python.org/es/3/library/tkinter.html#a-simple-hello-world-program

Si revisamos el código, veremos la forma más correcta y ordenada de trabajar con esta librería Tkinter.
Para aclarar, este programa a sido modificado por mi, pero solo traduciendo algunas palabras y funciones,
solo para acomodarlo a mi estilo.

Modificado por: Magh(Emgicraft)
"""

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master) # Con super llamamos a la clase padre.
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.btn = tk.Button(self)
        self.btn["text"] = "Hola Mundo\n(Clickeame)"
        self.btn["command"] = self.saludar
        self.btn.pack(side="top")

        self.btnSalir = tk.Button(self, text="Salir", fg="red",
                                  command=self.master.destroy)
        self.btnSalir.pack(side="bottom")

    def saludar(self):
        print("Hola a todos!")

ventana = tk.Tk()
app = Application(master=ventana)
app.mainloop()