import re

print("Dime tu correo electronico")
email = input()

regla = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

validacion = re.search(regla,email)

if validacion:
    print("Correo aceptado lo voy a guardar en nuestra base de datos")
else:
    print("Eso no es un correo electronico")
