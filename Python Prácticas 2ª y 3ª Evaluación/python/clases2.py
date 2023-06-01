#declaracion de clases

class Persona:

    def __init__ (self,nombre,edad,apellido,colorpelo): #lo que se le asigna cuando nace. Es el constructor
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.colorpelo = colorpelo


    def mePresento(self): #el usuario hace una accion
        print("Hola, mi nombre es"+self.nombre)
        
persona1 = Persona("Juan",0,"Lopez","negro")
persona2 = Persona("Jaime",3,"Garcia","rubio")

print(persona1.nombre)
print(persona2.nombre)


persona1.mePresento()
persona1.nombre = "Jorge"
persona1.mePresento()
