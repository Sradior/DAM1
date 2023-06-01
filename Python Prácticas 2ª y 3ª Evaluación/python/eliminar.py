
import sqlite3 as lite
import sys

conexion = lite.connect("loterias.sqlite3")

cursor = conexion.cursor()

cursor.execute("DELETE FROM Euromillones WHERE fecha = 07/02/2023;")

datos = cursor.fetchall()
