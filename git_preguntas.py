from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Preguntas")
root.geometry("400x500")
Label(root,text="Preguntas",font=("Arial","20","bold")).place(x=1,y=10)

def abrir_pagina():
    pagina=Toplevel(root)
    pagina.geometry("400x500")

    Label(pagina,text="1. ¿Cuántos lados tiene un triángulo?").place(x=10,y=10)
    spin1=Spinbox(pagina,values=("2","3","4"))
    spin1.place(x=10,y=40)

    Label(pagina,text="2. ¿Cuánto es 5+5?").place(x=10,y=80)
    spin2=Spinbox(pagina,values=("8","10","12"))
    spin2.place(x=10,y=110)

    Label(pagina,text="3. ¿Cuántos días tiene una semana?").place(x=10,y=150)
    spin3=Spinbox(pagina,values=("5","7","9"))
    spin3.place(x=10,y=180)

    texto=Label(pagina,text="")
    texto.place(x=10,y=240)

    Label(pagina,text="cuanto es 2+2").place(x=10,y=320)
    spin4=Spinbox(pagina,values=("2","3","4"))
    spin4.place(x=10, y=350)

    def respuestas():
        puntos=0

        if spin1.get()=="3":
            puntos+=1
        if spin2.get()=="10":
            puntos+=1
        if spin3.get()=="7":
            puntos+=1

        texto.config(text="Puntos "+str(puntos))

    Button(pagina,text="Enviar",command=respuestas).place(x=10,y=280)

def abrir_pagina2():
    pagina2=Toplevel(root)
    pagina2.geometry("400x500")

    Label(pagina2,text="1. Capital de Francia").place(x=10,y=10)
    combo1=ttk.Combobox(pagina2,values=("Madrid","Paris","Roma"))
    combo1.place(x=10,y=40)

    Label(pagina2,text="2. Color del cielo").place(x=10,y=80)
    combo2=ttk.Combobox(pagina2,values=("Rojo","Azul","Verde"))
    combo2.place(x=10,y=110)

    Label(pagina2,text="3. Animal que vuela").place(x=10,y=150)
    combo3=ttk.Combobox(pagina2,values=("Perro","Pájaro","Gato"))
    combo3.place(x=10,y=180)

    texto=Label(pagina2,text="")
    texto.place(x=10,y=240)

    def respuestas():
        puntos=0

        if combo1.get()=="Paris":
            puntos+=1
        if combo2.get()=="Azul":
            puntos+=1
        if combo3.get()=="Pájaro":
            puntos+=1

        texto.config(text="Puntos "+str(puntos))

    Button(pagina2,text="Enviar",command=respuestas).place(x=10,y=210)

def abrir_pagina3():
    pagina3=Toplevel(root)
    pagina3.geometry("400x500")

    respuesta1 = StringVar()
    respuesta2 = StringVar()

    Label(pagina3,text="1. ¿Cuánto es 2+2?").place(x=10,y=10)

    r1=Radiobutton(pagina3,text="3",value="3",variable=respuesta1)
    r1.place(x=10,y=40)

    r2=Radiobutton(pagina3,text="4",value="4",variable=respuesta1)
    r2.place(x=10,y=60)

    Label(pagina3,text="2. ¿Planeta donde vivimos?").place(x=10,y=100)

    r3=Radiobutton(pagina3,text="Marte",value="Marte",variable=respuesta2)
    r3.place(x=10,y=130)

    r4=Radiobutton(pagina3,text="Tierra",value="Tierra",variable=respuesta2)
    r4.place(x=10,y=150)

    texto=Label(pagina3,text="")
    texto.place(x=10,y=220)

    def respuestas():

        if respuesta1.get()=="4" and respuesta2.get()=="Tierra":
            texto.config(text="Todo correcto")

        elif respuesta1.get()=="4" or respuesta2.get()=="Tierra":
            texto.config(text="Una correcta")

        else:
            texto.config(text="Incorrecto")

    Button(pagina3,text="Enviar",command=respuestas).place(x=10,y=180)

def abrir_pagina4():
    pagina4=Toplevel(root)
    pagina4.geometry("400x500")

    Label(pagina4,text="1. Lenguaje de programación").place(x=10,y=10)

    respuesta1=StringVar()
    respuesta1.set("Seleccionar")

    menu1=OptionMenu(pagina4,respuesta1,"Python","HTML","CSS")
    menu1.place(x=10,y=40)

    Label(pagina4,text="2. Continente de Colombia").place(x=10,y=120)

    respuesta2=StringVar()
    respuesta2.set("Seleccionar")

    menu2=OptionMenu(pagina4,respuesta2,"Europa","Asia","America")
    menu2.place(x=10,y=150)

    texto=Label(pagina4,text="")
    texto.place(x=10,y=230)

    def respuestas():

        r1=respuesta1.get()
        r2=respuesta2.get()
        if r1=="Python" and r2=="America":
            texto.config(text="Correcto")
        if r1=="Python" or r2=="America":
            texto.config(text="Solo 1 correcto")
        elif r1=="Seleccionar" or r2=="Seleccionar":
            texto.config(text="Selecciona ambas respuestas")
        else:
            texto.config(text="Incorrecto")

    Button(pagina4,text="Enviar",command=respuestas).place(x=10,y=200)

Button(root,text="Spinbox",command=abrir_pagina).place(x=60,y=450)
Button(root,text="Combobox",command=abrir_pagina2).place(x=120,y=450)
Button(root,text="Radiobutton",command=abrir_pagina3).place(x=200,y=450)
Button(root,text="Select",command=abrir_pagina4).place(x=290,y=450)

root.mainloop()