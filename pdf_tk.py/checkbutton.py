from tkinter import * 
root = Tk() 
root.title("Ventana principal") 
root.geometry("250x200") 
def seleccion(): 
    etiqueta1 = Label(root, text=control1.get()).pack() 
    etiqueta2 = Label(root, text=control2.get()).pack() 
    etiqueta3 = Label(root, text=control3.get()).pack() 
control1 = StringVar() 
control2 = StringVar() 
control3 = StringVar() 
opcion_1 = Checkbutton(root, text="Opcion 1", variable=control1, 
onvalue="Opcion 1 seleccionada", offvalue="Opcion 1 no seleccionada") 
opcion_1.pack() 
opcion_1.deselect() 
opcion_2 = Checkbutton(root, text="Opcion 2", variable=control2, 
onvalue="Opcion 2 seleccionada", offvalue="Opcion 2 no seleccionada") 
opcion_2.pack() 
opcion_2.deselect() 
opcion_3 = Checkbutton(root, text="Opcion 3", variable=control3, 
onvalue="Opcion 3 seleccionada", offvalue="Opcion 3 no seleccionada") 
opcion_3.pack() 
opcion_3.deselect() 
muestra_seleccion = Button(root, text="Mostrar selección", 
command=seleccion).pack() 
mainloop() 