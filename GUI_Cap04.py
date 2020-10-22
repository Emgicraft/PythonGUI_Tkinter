"""
Este programa está basado en los siguientes vídeo tutoriales:
    Curso Python. Interfaces gráficas IV. Vídeo 45

Autor: Magh(Emgicraft)
"""

import tkinter as tk

raiz = tk.Tk()

raiz.title("PythonGUI con Tkinter")
raiz.iconbitmap("Recursos/MCServer-icon-64x64.ico")
raiz.geometry("720x480")

frame = tk.Frame(raiz)
frame.pack(fill="both", expand=True)

"""
Se puede hacer así:
    txt1 = tk.Label(frame, text="Nombre", fg="red", font=("Comic Sans MS", 14))
    #txt1.place(x=10, y=4) # Ubicación manual.
    txt1.grid(row=0, column=0, padx=10, pady=10) # Ubicación por grilla.

    boxName = tk.Entry(frame)
    #box1.place(x=100, y=12) # Ubicación manual.
    boxName.grid(row=0, column=1, padx=10, pady=10) # Ubicación por grilla.

Pero vamos a automatizar el proceso.
"""
def aplicaGrid(fils, columns, px, py, *ele):
    e = iter(ele)
    for fil in range(fils):
        for col in range(columns):
            next(e).grid(row=fil, column=col, padx=px, pady=py)

txtNombre = tk.Label(frame, text="Nombre", fg="red", font=(14))
txtApellido = tk.Label(frame, text="Apellido", fg="red", font=(14))

boxName = tk.Entry(frame)
boxApellido = tk.Entry(frame)

aplicaGrid(2, 2, 10, 10, txtNombre, boxName, txtApellido, boxApellido)

raiz.mainloop()