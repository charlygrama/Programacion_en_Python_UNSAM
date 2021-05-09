# -*- coding: utf-8 -*-
# 5.3 El album de Figuritas
import random
import numpy as np

#%%
### Ejercicio 5.9: Crear
figus_total = 5 

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=int)
    return album

#%%
### Ejercicio 5.10: Incompleto
def  album_incompleto(A):
    if 0 in A:
        incompleto = True
    else:
        incompleto = False
    return incompleto

#%%
### Ejercicio 5.11: Comprar 
comprada = []
def comprar_figu(figus_total):
    comprada = random.randint(1, figus_total)
    return comprada 

#%%
### Ejercicio 5.12: Cantidad de compras 
def cuantas_figus(figus_total):
    album_nuevo = crear_album(figus_total)
    cant_compradas = 0
    incompleto = True
    while incompleto:
        for i, comprada in enumerate(album_nuevo):    
            comprada = comprar_figu(figus_total)
            cant_compradas += 1
            if not comprada in album_nuevo:
                album_nuevo[i] = 1
            else:
                album_nuevo[i] +=  1
                
        incompleto = album_incompleto(album_nuevo)
    return cant_compradas, album_nuevo 

album = crear_album(figus_total)
incompleto = album_incompleto(album)
comprada = comprar_figu(figus_total)
cant_compradas = cuantas_figus(figus_total)
print(cant_compradas)

# compradas, album = cuantas_figus(n)
#%%
