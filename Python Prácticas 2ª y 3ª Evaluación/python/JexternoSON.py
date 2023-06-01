import json

micadena = '{"luis":"luis@gmail.com","pablo":"pablo@gmail.com"}'

carga = json.loads(micadena)

print(type(micadena))
print(type(carga))

print(carga["pablo"])

