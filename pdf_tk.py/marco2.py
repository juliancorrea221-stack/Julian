from tkinter import * 
root = Tk() 
def click_boton():
    texto=Label(root,text="No presione el boton").grid(row=0,column=1)
boton1 = Button(root, text="No presiones el botón", bg="red", padx=100, 
pady=25, command=click_boton).grid(row=1, column=2) 
# Marco 1 
marco_principal1 = Frame() 
marco_principal1.grid(row=0, column=0) 
marco_principal1.config(width="100", height="100") 
marco_principal1.config(bg="red") 
# Marco 2 
marco_principal2 = Frame() 
marco_principal2.grid(row=0, column=1) 
marco_principal2.config(width="100", height="100") 
marco_principal2.config(bg="blue") 
# Marco 3 
marco_principal3 = Frame() 
marco_principal3.grid(row=1, column=0) 
marco_principal3.config(width="100", height="100") 
marco_principal3.config(bg="yellow") 
# Marco 4 
marco_principal4 = Frame() 
marco_principal4.grid(row=1, column=1) 
marco_principal4.config(width=100, height="100") 
marco_principal4.config(bg="green") 
# Marco 5 
marco_principal5 = Frame() 
marco_principal5.grid(row=2, column=0) 
marco_principal5.config(width=100, height="100") 
marco_principal5.config(bg="orange") 
# Marco 6 
marco_principal6 = Frame() 
marco_principal6.grid(row=2, column=1) 
marco_principal6.config(width=100, height="100") 
marco_principal6.config(bg="black") 

root.mainloop() 