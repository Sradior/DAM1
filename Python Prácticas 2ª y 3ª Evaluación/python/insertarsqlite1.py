#para poder trabajar con bbdd
import sqlite3 as lite
import sys
#me conecto a la bbdd llamada agenda, dentro de mi carpeta de Python
conexion = lite.connect("agenda.sqlite3")
#al realizar una conexión y un SELECT se ha creado el archivo agenda.sqlite
cursor = conexion.cursor()
#establezco un cursor para saber en qué punto de la bbdd voy a trabajar
cursor.execute("SELECT * FROM contactos;") #lenguaje SQL entre paréntesis en verde

datos = cursor.fetchall() #contiene lo que me devuelve la bbdd

for i in datos:
    print("ID:",i[0],"\t nombre:",i[1],"\t telefono: ",i[2],"\t email:",i[3])
