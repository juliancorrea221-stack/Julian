from tkinter import * 
root = Tk() 
root.title("Ventana principal") 
root.geometry("300x100") 
def enviar_boton(): 
    ventana_nueva = Toplevel() 
    ventana_nueva.title("Ventana secundaria") 
    ventana_nueva.geometry("300x200") 
    valor_entrada = entrada.get() 
    etiqueta = Label(ventana_nueva, text="El valor introducido en la ventana principal es: " + valor_entrada).grid(row=0) 
    cerrar_ventana = Button(root, text="Cerrar la ventana", command=ventana_nueva.destroy).grid(row=2) 
entrada = Entry(root, width=20) 
entrada.grid(row=0) 
envia = Button(root, text="Enviar", command=enviar_boton).grid(row=1) 
cerrar_root = Button(root, text="Cerrar ventana principal", 
command=root.destroy).grid(row=3) 
mainloop() 