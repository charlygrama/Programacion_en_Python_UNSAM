# -*- coding: utf-8 -*-
# 5.3 El album de Figuritas
import random
import numpy as np

#%%
### Ejercicio 5.9: Crear
def crear_album(figus_total):
    album = np.zeros(figus_total, dtype = int )
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
    comprada.append(random.randint(1, figus_total))
    return comprada 
#%%
### Ejercicio 5.12: Cantidad de compras 
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    cant_compradas = 0
    compradas = []
    incompleto = True
    while incompleto == True:
        compradas = comprar_figu(figus_total)
        cant_compradas += 1
        for i in album:
            if compradas in comprada:
                pass
            else:
                album[i] = comprada
        incompleto = album_incompleto(album)
    return cant_compradas, album  

n = 5
compradas, album = cuantas_figus(n)
#%%
