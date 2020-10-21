"""
Este programa está basado en los siguientes vídeo tutoriales:
    Curso Python. Interfaces gráficas III. Vídeo 44
    Curso Python. Interfaces gráficas IV. Vídeo 45

Autor: Magh(Emgicraft)
"""

import tkinter as tk

raiz = tk.Tk()

raiz.title("PythonGUI con Tkinter")
#raiz.resizable(False, False)
raiz.iconbitmap("Recursos/MCServer-icon-64x64.ico")
raiz.geometry("720x480")
raiz.config(bg="blue")

frame = tk.Frame()
frame.pack(fill="both", expand=True)
frame.config(width="480", height="360", bg="red",
             bd=17, relief="groove",
             cursor="pirate")

raiz.mainloop()