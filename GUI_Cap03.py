"""
Este programa está basado en el siguiente vídeo tutorial:
    Curso Python. Interfaces gráficas III. Vídeo 44

Autor: Magh(Emgicraft)
"""

import tkinter as tk

raiz = tk.Tk()

raiz.title("PythonGUI con Tkinter")
#raiz.resizable(False, False)
raiz.iconbitmap("Recursos/MCServer-icon-64x64.ico")
raiz.geometry("720x480")
raiz.config(bg="blue")

frame = tk.Frame(raiz, width="480", height="360", bg="red")
#frame.pack(fill="both", expand=True)
frame.pack()
#frame.config(width="480", height="360", bg="red", bd=17, relief="groove", cursor="pirate")

#img1 = tk.PhotoImage(file="Recursos/MCServer-icon-64x64.png")
img1 = tk.PhotoImage(file="Recursos/Psycho-Pass_326x254 - 02.png")
txt1 = tk.Label(frame, image=img1)
#txt1 = tk.Label(frame, text="Texto de Prueba", fg="red", font=("Comic Sans MS", 16))
#txt1.pack() # Si uso "pack", ocupa todo el frame y lo redimensiona.
txt1.place(x=10, y=10) # Con "place" podremos ubicarlo dentro del frame.

raiz.mainloop()