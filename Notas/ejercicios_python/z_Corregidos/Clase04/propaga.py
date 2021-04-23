# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 16:12:41 2021

@author: Christian
"""

#%%
def propagar(lista):
    
    '''En el ciclo while, primero agrego el elemento a una lista nueva, para 
    no modificar la entrada. Luego comparo si es un 0, que es el único numero 
    que puede cambiar. y pregunto si el numero anterior es un 1, si lo es 
    cambio el elemento de la nueva lista por 1. luego con el otro while recorro
    hacia el otro lado.'''
    i = 0
    listaf = []
    
    while i < len(lista):
        listaf.append(lista[i])
     
        if listaf[i] == 0:
            if i - 1 > 0 and listaf[i-1] == 1:
                listaf[i] = 1
        
        i += 1
        
    while i > 0:
        i -= 1
        if listaf[i] == 0:
            if i + 1 < len(listaf) and (listaf[i+1] == 1):
                listaf[i] = 1
                        
    return listaf

l1 = [ 0, 0, 0, 1, 0, 0]
l1p = propagar(l1)

print(f'Si partimos de {l1} y la propagamos obtemos {l1p}')


l2 = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
l2p = propagar(l2)

print(f'Si partimos de {l2} y la propagamos obtemos {l2p}')

