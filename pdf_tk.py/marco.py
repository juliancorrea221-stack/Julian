from tkinter import * 
root = Tk() 
root.geometry="600x500"
texto=Label(root,text="Ingrese el usuario y la contraseña",fg="red")
texto.grid(row=0,column=0)
entrada = Entry(root,width=100,bg="yellow",fg="red")
entrada.grid(row=1, column=0) 
entrada_2=Entry(root,width=100,bg="yellow",fg="black",show=".")
entrada_2.grid(row=2,column=0)
def click_boton(): 
    texto=Label(root,text="Se envio correctamente").grid(row=4,column=0)

boton=Button(root,text="Enviar",padx=100,pady=25,command=click_boton,bg="red").grid(row=3,column=0)
root.mainloop()