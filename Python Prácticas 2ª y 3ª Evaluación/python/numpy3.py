import numpy as np
import array as arr

coleccion1 = np.array(['Juan','Jorge','Julia','Javier','Jose','Jacobo'])

coleccion2= np.array(['Pablo', 'Pedro','Paco','Pio','Paloma'])

juntado = np.concatenate((coleccion1,coleccion2))

busqueda = np.where(juntado == 'Javier')
print(busqueda)
