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
micursor.execute("INSERT INTO productos VALUES(NULL, Libreta, 59, 4")
mibd.commit()
