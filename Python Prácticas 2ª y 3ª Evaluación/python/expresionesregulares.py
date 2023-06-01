import re

mitexto = "David"
busqueda = re.search("no",mitexto) #regular expressions repasar tabla
print(busqueda)
if busqueda:
    print("He encontrado una coincidencia")
else:
    print("No hay coincidencias")
