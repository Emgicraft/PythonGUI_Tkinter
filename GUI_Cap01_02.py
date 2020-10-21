"""
Este programa está basado en los siguientes vídeo tutoriales:
    Curso Python. Interfaces gráficas I. Vídeo 42
    Curso Python. Interfaces gráficas II. Vídeo 43

Autor: Magh(Emgicraft)
"""

import tkinter as tk

# Instancio la ventana:
raiz = tk.Tk()
#raiz2 = tk.Tk()
# Es posible crear otra ventana y las dos se ejecutan al mismo tiempo pero separadas.

raiz.title("PythonGUI con Tkinter")
# Permite o no la redimension en x o y de la ventana raiz:
raiz.resizable(False, False) # (x, y) -> (True, True) por defecto.
raiz.iconbitmap("Recursos/MCServer-icon-64x64.ico")
# Defino la geometría de la ventana raíz:
raiz.geometry("720x480")
# Con config se pueden cambiar varias cosas, por ahora solo el fondo:
raiz.config(bg="blue")

# Tener claro que la raíz es dónde estará todo el contenido de la ventana.
# Y el frame es como el contenedor para los botones y demás.
# El cual, estará dentro de la raíz.

frame = tk.Frame()
# Con solo esto le decimos que se enpaquete con la raiz:
#frame.pack(side="right", # Adicionalmente se puede indicar su posición en la raíz.
#           anchor="s") # N W S E <- Cardinales

#frame.pack(fill="y", # x y both None <- x puede funcionar sin "expand"
#           expand=True) # Le decimos que se expanda y normalmente va con fill
# Dejaremos al frame expandido en toda la raiz:

frame.pack(fill="both", expand=True)
frame.config(width="480", height="360", bg="red",
             bd=17, # Este es el grosor del borde.
             relief="groove", # Tipo de borde.
             cursor="pirate") # Tipo de cursor para cuando esté dentro del frame. Otro: "hand2"

raiz.mainloop()

# Lo que haya después se ejecutará al cerrar la ventana(s)
#raiz2.mainloop() # Incluso si hay este bucle al final.