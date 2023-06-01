import mysql.connector as my

mibd = my.connect(
    host = "localhost",
    port = "3306",
    user = "cursoaplicacionesweb",
    password = "cursoaplicacionesweb",
    database = "cursoaplicacionesweb"
    )
print(mibd)
micursor = mibd.cursor()
micursor.execute("UPDATE productos SET cantidad = '5' where identificador = '2'")
mibd.commit()
