"""
Este programa está basado en los siguientes vídeos tutoriales:
    Curso Python. Interfaces gráficas IV. Vídeo 45
    Curso Python. Interfaces gráficas V. Vídeo 46

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
scrollVert.grid(row=5, column=3, padx=0, pady=10, sticky="news") # Posicionando por grid.
#scrollVert.place(x=105, y=0) # Podriamos posicionarlo manualmente.

# Para que el scroll se posicione adecuadamente, usamos:
boxComentarios.config(yscrollcommand=scrollVert.set)

# Ahora a crear botones:
btnEnviar = tk.Button(frame, text="Enviar")
#btnEnviar.place(x=150, y=300)
btnEnviar.grid(row=6, column=4, padx=10, pady=10)

btnSalir = tk.Button(frame, text="Salir xD", command=raiz.quit)
btnSalir.grid(row=0, column=0, padx=10, pady=10)

# Defino una función para salir y con parámetro para indicar la raiz:
def salir(queRaiz):
    print("Saliendo del programa de prueba...")
    queRaiz.quit()
    print("Cerrado.")

btnPrueba = tk.Button(raiz)
btnPrueba["text"] = "Probando" # Usamos el acceso por clave.
#btnPrueba["command"] = lambda: salir(raiz) # Esta es una opción válida.

from functools import partial

btnPrueba["command"] = partial(salir, raiz) # Y está es otra opción también válida.
btnPrueba.pack()

aplicaGrid(5, 2, 10, 10, "nes", txtNombre, boxName,
                                txtApellido, boxApellido,
                                txtEdad, boxEdad,
                                txtContra, boxContra,
                                txtComentario, boxComentarios)

# Con las siguientes líneas aparecen cosas interesantes:
print(txtNombre.keys()) # Todos los parámetros que puedo usar con ese tipo de widget.
print("-"*100)
print(boxName.config()) # Muestra todos los parámetros y tuplas asociadas en forma de diccionario.
print("-"*100)
print(boxComentarios) # Directamente me muestra (creo) al objeto Tk o tcl.
print(scrollVert) # Lo mismo que el anterior.

# Por último, inciamos la ventana:
raiz.mainloop()