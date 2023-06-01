archivo = open ("agendatelefonica.txt",'r')

linea = archivo.read()
print(linea)

partido = linea.split(",") #split nos permite convertir un print/string a un list
print(partido[0])
