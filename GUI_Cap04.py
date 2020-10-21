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

frame = tk.Frame(raiz, width="480", height="360")
frame.pack(fill="both", expand=True)

raiz.mainloop()