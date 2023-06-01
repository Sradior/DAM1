import mysql.connector as my
import matplotlib.pyplot as plt
import numpy as np
mibd = my.connect(
    host = "localhost",
    port = "3306",
    user = "cursoaplicacionesweb",
    password = "cursoaplicacionesweb",
    database = "cursoaplicacionesweb"
    )
micursor = mibd.cursor()

micursor.execute("SELECT * FROM apellidos GROUP BY Apellido ORDER BY ap1 LIMIT 30;")
miresultado = micursor.fetchall()
longaniza = "'hola'"
performance = [0]

for i in miresultado:
        
        longaniza += ",'"+str(i[1])+"'"
        performance.append(i[0])

people = eval(longaniza)
print(people)
plt.rcdefaults()
fig, ax = plt.subplots()

# Example data

y_pos = np.arange(len(people))

print(performance)
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()
