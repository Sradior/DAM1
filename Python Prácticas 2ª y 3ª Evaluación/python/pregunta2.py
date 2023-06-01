#importamos librerias
from PIL import Image
import math

#abrimos una imagen que hayamos descargado en la carpeta del examen
imagen = Image.open("prueba.jpg") 
pixeles = imagen.load() #cargo los pixeles de la imagen
print(imagen.size)

print(pixeles[0,0])

altura = imagen.size[1] 
anchura = imagen.size[0]
## Pediré cada pixel a partir de el plano con coordenadas x e y y entonces
## Sumare R+G+B/3 y si me da por encima de 127 será blanco y sino negro
## O al revés que no recuerdo bien
for x in range(0,anchura):
    for y in range(0,altura):
        rojo = pixeles[x,y][0]
        verde = pixeles[x,y][1]
        azul = pixeles[x,y][2]
        color = math.floor((rojo+verde+azul)/3)

        if color > 127:
            rojo = 255
            verde = 255
            azul = 255

        else:
            rojo = 0
            verde = 0
            azul = 0

        pixeles[x,y] = (rojo,verde,azul)

imagen.save("resultado.jpg") ## Por último guardo la imagen nueva con los pixeles
