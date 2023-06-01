import re

email = "obareaz@gmail.com"
regla = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

validacion = re.search(regla,email)


print(validacion)




