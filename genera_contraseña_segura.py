import random
import string
from tkinter import *

def generar_contrasena():
    longitud = int(entry_longitud.get())
    incluir_mayus = var_mayus.get()
    incluir_numeros = var_numeros.get()
    incluir_simbolos = var_simbolos.get()
    
    caracteres = string.ascii_lowercase
    if incluir_mayus:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    label_contrasena.config(text=f"Contraseña generada: {contrasena}")

ventana = Tk()
ventana.title("Generador de Contraseñas")

Label(ventana, text="Longitud:").pack()
entry_longitud = Entry(ventana)
entry_longitud.pack()

var_mayus = BooleanVar()
Checkbutton(ventana, text="Incluir mayúsculas", variable=var_mayus).pack()

var_numeros = BooleanVar()
Checkbutton(ventana, text="Incluir números", variable=var_numeros).pack()

var_simbolos = BooleanVar()
Checkbutton(ventana, text="Incluir símbolos", variable=var_simbolos).pack()

Button(ventana, text="Generar Contraseña", command=generar_contrasena).pack()

label_contrasena = Label(ventana, text="")
label_contrasena.pack()

ventana.mainloop()
