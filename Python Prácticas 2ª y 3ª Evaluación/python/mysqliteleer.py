#para poder trabajar con bbdd
import sqlite3 as lite
import sys
#me conecto a la bbdd llamada agenda, dentro de mi carpeta de Python
conexion = lite.connect("agenda.sqlite3")
#al realizar una conexión y un SELECT se ha creado el archivo agenda.sqlite
cursor = conexion.cursor()
#establezco un cursor para saber en qué punto de la bbdd voy a trabajar
cursor.execute("SELECT SQLITE_VERSION()") #lenguaje SQL entre paréntesis en verde

datos = cursor.fetchone() #contiene lo que me devuelve la bbdd
print("La version de SQLite es:",datos)
