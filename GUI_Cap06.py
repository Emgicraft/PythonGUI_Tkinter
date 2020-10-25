"""
Este programa está basado en el siguiente vídeo tutorial:
    Curso Python. Interfaces gráficas VI. Vídeo 47
    Curso Python. Interfaces gráficas VII. Vídeo 48

Autor: Magh(Emgicraft)
"""

import tkinter as tk

# ----------------------------------Creo ventana y frame----------------------------------
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.iconbitmap("Recursos/MCServer-icon-64x64.ico")
ventana.geometry("250x250")

frame = tk.Frame(ventana)
frame.pack()

# ----------------------------------Parámetros globales----------------------------------
paddingX, paddingY = 5, 10
anchoBtns = 4

# ----------------------------------Pantalla----------------------------------
pantalla = tk.Entry(frame)
pantalla.config(bg="black", fg="green", justify="right", font=(10)) # El num en font no afecta.
pantalla.grid(row=0, column=0, padx=paddingX, pady=paddingY, columnspan=5, sticky="news")

# ----------------------------------Creo los Botones----------------------------------
btnNums = []
def btnNumerics(func, elFrame, cant, ancho):
    for num in range(cant):
        btnNums.append(func(elFrame, text=str(num), width=ancho))
        print("Botón #{} creado.".format(num))

btnNumerics(tk.Button, frame, 10, anchoBtns) # Creo los diez primeros botones de golpe. ;v | Del 0 al 9
btnPunto = tk.Button(frame, text=".", width=anchoBtns)
btnSum = tk.Button(frame, text="+", width=anchoBtns)
btnRes = tk.Button(frame, text="-", width=anchoBtns)
btnMul = tk.Button(frame, text="*", width=anchoBtns)
btnDiv = tk.Button(frame, text="/", width=anchoBtns)
btnIgual = tk.Button(frame, text="=", width=anchoBtns)

# ----------------------------------Agrego los botones al Frame----------------------------------
def aplicaGrid(fils, columns, px, py, pos, *ele):
    e = iter(ele)
    for fil in range(1, fils+1):
        for col in range(1, columns+1):
            next(e).grid(row=fil, column=col, padx=px, pady=py, sticky=pos)

aplicaGrid(4, 4, paddingX, paddingY, "news", btnNums[7], btnNums[8], btnNums[9], btnDiv,
                                             btnNums[4], btnNums[5], btnNums[6], btnMul,
                                             btnNums[1], btnNums[2], btnNums[3], btnRes,
                                             btnNums[0], btnPunto, btnIgual, btnSum)

# ----------------------------------Llamo al bucle----------------------------------
ventana.mainloop()