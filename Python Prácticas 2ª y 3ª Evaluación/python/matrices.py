import numpy as np

coleccion = np.array(['Juan','Jorge','Julia','Javier','Jose','Jacobo'])

coleccion2 = np.array(['Pedro','Antonio','Andrea','Rodrigo','Fernando','Lucia'])

juntado = np.concatenate((coleccion,coleccion2))

buqueda = np.where(juntado == 'Antonio')
