import mysql.connector as my

mibd = my.connect(
    host= "localhost",
    user= "Oscar",
    password = "Oscar"
    )
print(mibd)
