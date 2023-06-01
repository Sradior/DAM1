import os
from PIL import Image
import math 

for root, dirs, files in os.walk("./retocadas"): #listar las imágenes que hay en una carpeta
    for filename in files:
        print(filename)
        image = Image.open("./retocadas"+filename)
        pixeles = imagen.load()
        altura = imagen.size[1]
        anchura = imagen.size[0]
        for x in range(0,anchura):
            for y in range(0,altura):
                rojo = pixeles[x,y][0]
                verde = pixeles[x,y][1]
                azul = pixeles[x,y][2]
                color = math.floor((roj+verde+azul)/3)
                rojo = color
                verde = color
                azul = color
                pixeles[x,y] = (rojo,verde,azul)
        imagen.save("./retocadas"+filename)
    contador+= 1                
