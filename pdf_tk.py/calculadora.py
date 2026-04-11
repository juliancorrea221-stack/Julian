from tkinter import * 
root = Tk() 
root.title("Calculadora básica") 
def envia_boton(valor): 
    anterior =pantalla.get() 
    pantalla.delete(0, END) # Borra la pantalla 
    pantalla.insert(0, str(anterior) + str(valor)) 
def igual(): 
    global num2 
    num2 = pantalla.get() 
    pantalla.delete(0, END) 
    if operacion == "+": 
     pantalla.insert(0, float(num1) + float(num2)) 
    if operacion == "-": 
     pantalla.insert(0, float(num1) - float(num2)) 
    if operacion == "*": 
     pantalla.insert(0, float(num1) * float(num2)) 
    if operacion == "/": 
     pantalla.insert(0, float(num1) / float(num2)) 
def suma(): 
    global num1 
    global operacion 
    num1 = pantalla.get() 
    num1 = float(num1) 
    pantalla.delete(0, END) 
    operacion = "+" 
def resta(): 
    global num1 
    global operacion 
    num1 = pantalla.get() 
    num1 = float(num1) 
    pantalla.delete(0, END) 
    operacion = "-" 
def multiplicacion(): 
    global num1 
    global operacion 
    num1 = pantalla.get() 
    num1 = float(num1) 
    pantalla.delete(0, END) 
    operacion = "*" 
def division(): 
    global num1 
    global operacion 
    num1 = pantalla.get() 
    num1 = float(num1) 
    pantalla.delete(0, END) 
    operacion = "/" 
pantalla =Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=('arial', 18, 'bold')) 
pantalla.grid(row=0, padx=2, pady=2, columnspan=4) 
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:envia_boton(1)).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:envia_boton(2)).grid(row=1, column=1, padx=1, pady=1) 
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:envia_boton(3)).grid(row=1, column=2, padx=1, pady=1) 
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:envia_boton(4)).grid(row=2, column=0, padx=1, pady=1) 
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:envia_boton(5)).grid(row=2, column=1, padx=1, pady=1) 
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:envia_boton(6)).grid(row=2, column=2, padx=1, pady=1) 
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:envia_boton(7)).grid(row=3, column=0, padx=1, pady=1) 
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:envia_boton(8)).grid(row=3, column=1, padx=1, pady=1) 
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:envia_boton(9)).grid(row=3, column=2, padx=1, pady=1) 
boton_0 = Button(root, text="0", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:envia_boton(0)).grid(row=4, column=1, padx=1, pady=1) 
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", borderwidth=0, cursor="hand2", command=lambda: envia_boton(".")).grid(row=4, column=2, padx=1, pady=1) 
boton_igual = Button(root, text="=", width=9, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2",command=lambda:igual()).grid(row=4, column=0, padx=1, pady=1) 
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda:suma()).grid(row=1, column=3, padx=1, pady=1) 
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda:resta()).grid(row=2, column=3, padx=1, pady=1) 
boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda:multiplicacion()).grid(row=3, column=3, padx=1, pady=1) 
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda:division()).grid(row=4, column=3, padx=1, pady=1) 
mainloop() 