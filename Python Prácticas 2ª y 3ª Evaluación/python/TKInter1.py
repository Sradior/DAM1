from tkinter import *
#tanto Frame como Label,etc, son posibles gracias al import tkinter
marco = Frame(width=300,height=300)
marco.pack(padx=30,pady=30) #SIEMPRE habrá que empaquetarse el frame

titulo = Label(marco,text="Programa v0.1",fg="black",font =("Arial,Verdana,sans-serif",24))
titulo.pack(side=TOP) #fonts que hay dentro de nuestro S.O.

autor = Label (marco, text = "Oscar Barea",fg="green",font =("Arial,Verdana,sans-serif",14))
autor.pack(side=TOP)

#se puede recortar una imagen, por ejemplo, en el Gimp y así escalarla bien
foto = PhotoImage(file="guitarra.png",width=300,height=300)


textofoto = Label(marco,image=foto)
textofoto.pack(side=TOP)

mainloop() #arranca un programa en ventanas y de fondo un bucle infinito para escuchadores de eventos

