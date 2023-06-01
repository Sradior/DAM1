from tkinter import *
import sqlite3 as lite
import sys

def guarda(nombre,telefono,email):
    conexion = lite.connect("agenda.sqlite3")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO contactos VALUES(NULL,'Juan','657674546','juan@juan.com');")
    cursor.execute("INSERT INTO contactos VALUES(NULL,'"+nombre+"','"+telefono+"','"+email+"');")
    conexion.commit() #str es string #se usa "nombre", etc, para que salga cualquier nombre que se introduzca, no solamente el de Juan, Lopez, etc.

def lee():
    print("voy a leer la base de datos")
    conexion = lite.connect("agenda.sqlite3")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM contactos;")
    agenda = ""
    datos = cursor.fetchall()
    for i in datos:
        agenda += str("Identificador"+i[0]+"\t nombre"+i[1]+"\t telefono"+i[2]+"\t email"+i[3])
    titulodevuelve.insert = (INSERT,agenda)

marco = Frame(width=300,height=300)
marco.pack(padx=30,pady=30)

titulo = Label(marco,text="Programa v0.1",fg="black",font =("Arial,Verdana,sans-serif",24))
titulo.pack(side=TOP)

autor = Label (marco, text = "Oscar Barea",fg="green",font =("Arial,Verdana,sans-serif",14))
autor.pack(side=TOP)

foto = PhotoImage(file="guitarra.png",width=300,height=300)

textofoto = Label(marco,image=foto)
textofoto.pack(side=TOP)

tunombre = Label(marco,text="Introduce tu nombre",fg="black",font =("Arial,Verdana,sans-serif",12))
tunombre.pack(side=TOP)
campotunombre = Entry(marco)
campotunombre.pack(side=TOP)

tutelefono = Label(marco,text="Introduce tu telefono",fg="black",font =("Arial,Verdana,sans-serif",12))
tutelefono.pack(side=TOP)
campotutelefono = Entry(marco)
campotutelefono.pack(side=TOP)

tuemail = Label(marco,text="Introduce tu email",fg="black",font =("Arial,Verdana,sans-serif",12))
tuemail.pack(side=TOP)
campotuemail = Entry(marco)
campotuemail.pack(side=TOP)

boton = Button (marco,text="Pulsa para guardar",command=lambda:guarda(campotunombre.get(),campotutelefono.get(),campotuemail.get()))
boton.pack(side=TOP,padx=10,pady=10)

titulo2 = Label(marco,text="Dame los resultados de la base de datos",fg="black",font =("Arial,Verdana,sans-serif",24))
titulo2.pack(side=TOP)

botonresultados = Button (marco,text="Devuelve los registros",command=lambda:lee())
botonresultados.pack(side=TOP,padx=10,pady=10)

titulodevuelve = Text(marco,height=20,width=20)
titulodevuelve.pack(side=TOP)



mainloop()
