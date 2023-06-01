from PIL import Image
import math
####### Bloc de notas apuntes
####### [0]rojo, [1]Verde, [2]Azul, [3]Transparencia
imagenvertical = Image.open("caras/vertical.png")
pixelesverticales = imagenvertical.load()

imagenhorizontal = Image.open("caras/horizontal.png")
pixeleshorizontales = imagenhorizontal.load()

imagendiagonal1 = Image.open("caras/diagonal1.png")
pixelesdiagonal1 = imagendiagonal1.load()

imagendiagonal2 = Image.open("caras/diagonal2.png")
pixelesdiagonal2 = imagendiagonal2.load()

imagen = Image.open("caras/rubius.png")
pixeles = imagen.load()

imagenresultado = Image.open("caras/resultado.png")
pixelesresultado = imagenresultado.load()

print(imagen.size)

print(pixeles[0,0])

altura = imagen.size[1]
anchura = imagen.size[0]

numeropixelesverticales = 0
numeropixeleshorizontales = 0
numeropixelesdiagonales1 = 0
numeropixelesdiagonales2 = 0

#VERTICAL #bucle "for" para correr los píxeles tanto en horizontal como en vertical
for superx in range(0,247): #no son 256 (tamaño imagen) para que así no se salga de la capa en gimp
    for supery in range(0,247):
        suma = 0;
        valor=0
        for x in range (0,7):
            for y in range (0,7):
                if pixelesverticales[x,y][3] != 0: #valídame si en el píxel en el que estás, tiene color
                    valor = 0
                    valor = pixeles[superx+x,supery+y][0]-pixelesverticales[x,y][0]
                    suma += valor
        if abs(suma) > 500: #abs=absoluto
            pixelesresultado[superx+x,supery+y] = (0,0,0)
            numeropixelesverticales += 1
        else:
            pixelesresultado[superx+x,supery+y] = (255,255,255)

print("el numero de pixeles verticales es: "+str(numeropixelesverticales))

#HORIZONTAL
for superx in range(0,247):
    for supery in range(0,247):
        suma = 0;
        valor=0
        for x in range (0,7):
            for y in range (0,7):
                if pixeleshorizontales[x,y][3] != 0:
                    valor = 0
                    valor = pixeles[superx+x,supery+y][0]-pixeleshorizontales[x,y][0]
                    suma += valor
        if abs(suma) > 500:
            pixelesresultado[superx+x,supery+y] = (0,0,0)
            numeropixeleshorizontales += 1
        else:
            pixelesresultado[superx+x,supery+y] = (255,255,255)

print("el numero de pixeles horizontales es: "+str(numeropixeleshorizontales))

#DIAGONAL1
for superx in range(0,247):
    for supery in range(0,247):
        suma = 0;
        valor=0
        for x in range (0,7):
            for y in range (0,7):
                if pixelesdiagonal1[x,y][2] != 0:
                    valor = 0
                    valor = pixeles[superx+x,supery+y][0]-pixelesdiagonal1[x,y][0]
                    suma += valor
        if abs(suma) > 500:
            pixelesresultado[superx+x,supery+y] = (0,0,0)
            numeropixelesdiagonales1 += 1
        else:
            pixelesresultado[superx+x,supery+y] = (255,255,255)

print("el numero de pixeles diagonal1 es: "+str(numeropixelesdiagonales1))

#DIAGONAL2
for superx in range(0,247):
    for supery in range(0,247):
        suma = 0;
        valor=0
        for x in range (0,7):
            for y in range (0,7):
                if pixelesdiagonal2[x,y][2] != 0:
                    valor = 0
                    valor = pixeles[superx+x,supery+y][0]-pixelesdiagonal2[x,y][0]
                    suma += valor
        if abs(suma) > 500:
            pixelesresultado[superx+x,supery+y] = (0,0,0)
            numeropixelesdiagonales2 += 1
        else:
            pixelesresultado[superx+x,supery+y] = (255,255,255)

print("el numero de pixeles diagonal2 es: "+str(numeropixelesdiagonales2))
        
imagen.save("caras/rubius2.png")
imagenresultado.save("caras/resultado.png")
        
