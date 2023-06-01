import sqlite3 as lite
import sys
conexion = lite.connect("agenda.sqlite3")
cursor = conexion.cursor()
#uso ' ' porque ya he usado "" al principio y final de la acción
cursor.execute("DELETE FROM contactos WHERE Identificador = 3;")

conexion.commit()
