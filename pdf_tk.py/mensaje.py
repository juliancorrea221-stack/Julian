from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Este es el título de la ventana principal")

def muestra_ventana():
    askyesno(title="Una pregunta", message="Debería dejar el programa y salir a la calle?.") 

def muestra_ventana2():
    showinfo(title="Pregunta",message="Hola don tique")

def muestra_ventana3():
    showerror(title="Pregunta",message="Muchos uribistas hoy")
def muestra_ventana4():
    showwarning(title="Aquí va el título de cuadro de diálogo", message="Este")
def muestra_ventana5():
    askretrycancel(title="Una pregunta", message="Debería dejar el programa y salir a la calle?.") 

boton = Button(root, text="Mostrar mensaje", command=muestra_ventana)
boton2= Button(root, text="Mostrar mensaje", command=muestra_ventana2)
boton3= Button(root, text="Mostrar mensaje", command=muestra_ventana3)
boton4= Button(root, text="Mostrar mensaje", command=muestra_ventana4)
boton5= Button(root, text="Mostrar mensaje", command=muestra_ventana5)

boton.pack()
boton2.pack()
boton3.pack()
boton4.pack()
boton5.pack()

root.mainloop()