import re

####
print("Introduce un numero")
email = input()

regla = r'^([\s\d]+)$'

validacion = re.search(regla,email)

if validacion:
    print("Ok")
else:
    print("No ok")
