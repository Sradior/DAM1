import mysql.connector as my

mibd = my.connect(
    host = "localhost"
    port = "3306"
    user = "lenguajedemarcas1"
    password = "lenguajedemarcas1"
    database = "clasebasesdedatos"
    )
print(mibd)
micursor = mibd.cursor()
micursor.execute("SELECT * FROM cursos")
resultado = micursor.fetchall()
print(resultado)

for i in resultado:
    print("Tengo un resultado que es:")
    print(i)
