import numpy as np
import array as arr

coleccion1 = np.array(['Juan','Jorge','Julia','Javier','Jose','Jacobo'])

coleccion2= np.array(['Pablo', 'Pedro','Paco','Pio','Paloma'])

juntado = np.concatenate((coleccion1,coleccion2))

print(juntado)

separado = np.array_split(juntado,3) #lo parte en 3, se ve en shell

print("Que sepas que la primera parte del partido es")
print(separado[0])
print("Que sepas que la segunda parte del partido es")
print(separado[1])
print("Que sepas que la tercera parte del partido es")
print(separado[2])
