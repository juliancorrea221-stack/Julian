import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("150x150")

titulo1 = Label(root, text="Noroeste").pack(anchor=NW)
titulo2 = Label(root, text="Norte").pack(anchor=N)
titulo3 = Label(root, text="Noroeste").pack(anchor=NE)
titulo4 = Label(root, text="Oeste").pack(anchor=W)
titulo5 = Label(root, text="Centro").pack(anchor=CENTER)
titulo6 = Label(root, text="Este").pack(anchor=E)
titulo7 = Label(root, text="Sudeste"). pack(anchor=SE)
titulo8 = Label(root, text="Sur"). pack(anchor=S)



root.mainloop()