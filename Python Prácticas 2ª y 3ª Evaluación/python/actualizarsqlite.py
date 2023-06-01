import sqlite3 as lite
import sys
conexion = lite.connect("agenda.sqlite3")
cursor = conexion.cursor()
#uso ' ' porque ya he usado "" al principio y final de la acción
cursor.execute("UPDATE contactos SET telefono = '123456';")

conexion.commit()
