# -*- coding: utf-8 -*-
# 5.3 El album de Figuritas
import random
import numpy as np
#%%
### Ejercicio 5.9: Crear
def crear_album(figus_total):
    album = np.zeros(figus_total)
    return album
   
# A = []
# album = crear_album(A) 
#%%
### Ejercicio 5.10: Incompleto
def album_incompleto(A):
    if 0 in A:
        incompleto = True
    else:
        incompleto = False

    return incompleto

# estado = album_incompleto(album)
#%%
### Ejercicio 5.11: Comprar 
def comprar_figu(figus_total):
    comprada = random.randint(1, figus_total)
    return comprada
    
# figu_comprada = comprar_figu(figus_total)
# # print('figu comprada: ', figu_comprada)    
#%%
### Ejercicio 5.12: Cantidad de compras 
def cuantas_figus(figus_total):
    nuevo_album = crear_album(figus_total)
    cant_compradas = 0
    incompleto = album_incompleto(nuevo_album)
    while incompleto == True:
        comprada = comprar_figu(figus_total)
        cant_compradas += 1
        if not comprada in nuevo_album:
            np.append(nuevo_album, comprada)
    return cant_compradas, nuevo_album  

n = 670
compradas, album = cuantas_figus(n)
#%%
