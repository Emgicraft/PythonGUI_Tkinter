"""
Este programa está basado en el siguiente vídeo tutorial:
    Curso Python. Interfaces gráficas IV. Vídeo 45

Autor: Magh(Emgicraft)
"""

import tkinter as tk

raiz = tk.Tk()

raiz.title("PythonGUI con Tkinter")
raiz.iconbitmap("Recursos/MCServer-icon-64x64.ico")
#raiz.geometry("720x480")

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

Pero vamos a automatizar el proceso, con la siguiente función podremos agregar los componentes
que deseemos y acomodarlos en una grilla con las dimensiones que le especifiquemos,
además también se podrá indicar el padding y la posición dentro de cada celda:
"""
def aplicaGrid(fils, columns, px, py, pos, *ele):
    e = iter(ele)
    for fil in range(1, fils+1):
        for col in range(1, columns+1):
            next(e).grid(row=fil, column=col, padx=px, pady=py, sticky=pos)

txtNombre = tk.Label(frame, text="Nombre:", fg="black", font=(14))
txtApellido = tk.Label(frame, text="Apellido:", fg="red", font=(14))
txtEdad = tk.Label(frame, text="Edad:", fg="blue", font=(14))
txtContra = tk.Label(frame, text="Contraseña:", fg="purple", font=(14))

boxName = tk.Entry(frame)
boxName.config(fg="red", justify="center") # Se puede modificar con parámetros similares a Label.
boxApellido = tk.Entry(frame)
boxEdad = tk.Entry(frame)
boxEdad.config(fg="blue", justify="right")
boxContra = tk.Entry(frame)
boxContra.config(show="F") # Muestra ese caracter en reemplazo de lo que se escriba.
# Ahora agregaremos una casilla especial, que admite varias líneas, junto con su Label:
txtComentario = tk.Label(frame, text="Comentario:", font=(14))
boxComentarios = tk.Text(frame, width=15, height=7) # Por defecto viene con un tamaño pero lo modificamos.
# Ahora agregamos su scroll:
scrollVert = tk.Scrollbar(frame, command=boxComentarios.yview) # Con esto solo lo instanciamos.
scrollVert.grid(row=5, column=3, padx=0, pady=10, sticky="news")
#scrollVert.place(x=105, y=0)

aplicaGrid(5, 2, 10, 10, "nes", txtNombre, boxName,
                                txtApellido, boxApellido,
                                txtEdad, boxEdad,
                                txtContra, boxContra,
                                txtComentario, boxComentarios)

raiz.mainloop()