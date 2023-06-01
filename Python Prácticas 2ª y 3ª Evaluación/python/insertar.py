
import sqlite3 as lite
import sys

conexion = lite.connect("loterias.sqlite3")

cursor = conexion.cursor()

cursor.execute("INSERT INTO Euromillones VALUES('07/02/2023','02','08','34','44','47','03','09');")

datos = cursor.fetchall()


conexion.commit()
