#Programa agenda


agenda = [["pedro","juan","alberto"]]

archivo = open("agendatelefonica.txt",'r')
for i in range(1,10):
    nuevalinea = archivo.read().split(",")  
    agenda.append(nuevalinea) #archivo.read leerá toda la lista del archivo

print (agenda)

def MiAgenda():
    
    print("Escoge una opcion")
    print("1.Introducir nuevo contacto")
    print("2.Ver contactos")
    print("3.Buscar contacto")
    opcion = input()

    if opcion == "1":
            
        print("Introduce el nombre")
        nombre = input()
        print("Introduce el numero de telefono")
        telefono = input()
        print("Introduce el correo")
        correo = input()
        agenda.append([nombre,telefono,correo])
        ##print (agenda)

        archivo = open("agendatelefonica.txt",'a')
        partesagenda = nombre+","+telefono+","+correo+"\n"
        archivo.write(str(partesagenda))
        archivo.close()

    if opcion == "2":
        for i in range(1,len(agenda)):
            print(agenda[i])
    
    MiAgenda()
    
MiAgenda()
