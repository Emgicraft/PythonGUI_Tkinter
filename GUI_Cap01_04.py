"""
Curso Python. Interfaces gráficas IV. Vídeo 45

Autor: Magh
"""

import tkinter as tk

raiz = tk.Tk()

raiz.title("GUI 04")
# Permite cambiar o no el tamaño en x o y de la ventana (raiz):
raiz.resizable(True, True) # (x, y) -> (False, False) por defecto.
raiz.iconbitmap("Recursos/MCServer-icon-64x64.ico")
raiz.geometry("720x480")
raiz.config(bg="blue")

raiz.mainloop()