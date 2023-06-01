from tkinter import *

def saluda():
    print("Hola, has pulsado el boton")

marco = Frame(width=300,height=300)
marco.pack(padx=30,pady=30)

titulo = Label(marco,text="Programa v0.1",fg="black",font =("Arial,Verdana,sans-serif",24))
titulo.pack(side=TOP)

autor = Label (marco, text = "Oscar Barea",fg="green",font =("Arial,Verdana,sans-serif",14))
autor.pack(side=TOP)

foto = PhotoImage(file="guitarra.png",width=300,height=300)


textofoto = Label(marco,image=foto)
textofoto.pack(side=TOP)

boton = Button (marco,text="Pulsa aqui",command=saluda)
boton.pack(side=TOP,padx=10,pady=10)

mainloop()
