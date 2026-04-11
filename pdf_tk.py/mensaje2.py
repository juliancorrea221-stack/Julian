from tkinter import * 
from tkinter.messagebox import * 
root = Tk() 
root.title("Este es el título de la ventana principal") 
def muestra_ventana(): 
    respuesta = askquestion(title="Pregunta seria", message="Debería dejar el programa y salir a la calle?.") 
    if respuesta == "no": 
     showinfo(title="¡A segujir programando!", message="Estupendo, eligió la respuesta correcta.") 
    else: 
      askretrycancel(title="Botón equivoado",message="Haga click en 'Reintenar' para seguir programando.") 
boton1 = Button(root, text="Enviar", command=muestra_ventana, width=75).pack() 
root.mainloop() 
