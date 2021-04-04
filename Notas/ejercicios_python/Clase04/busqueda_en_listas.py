# -*- coding: utf-8 -*-
# Ejercicio 4.6: Búsquedas de un elemento

def buscar_u_elemento(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e  and i > pos: # si encontramos a e y esta en un indice mayor
            pos = i  # guardamos su posición
    return pos # se devuelve valor de posición

def buscar_n_elemento(lista, e):
    '''devuelve la cantidad de veces que aparece el elemento en la lista'''
    rep = 0 # se inicia el contador en 0
    for i, z in enumerate(lista): # recorremos la lista
        if z == e: # si encontramos a e
            rep += 1  # aumentamos contador rep en 1
    return rep # se devuelve cantidad de repeticiones

### Ejercicio 4.7: Búsqueda de máximo y mínimo

def maximo(lista):
    '''Devuelve el máximo de una lista,
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista.
    m = -1000 # se iniciliza m
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

def minimo(lista):
    '''Devuelve el máximo de una lista,
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el minimo de los elementos a medida que recorro la lista.
    m = 1000 # se iniciliza m
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m

pos = buscar_u_elemento([1,2,3,2,3,4],3)
rep = buscar_n_elemento([1,1,1,2,3,4],1)
maxi = maximo([-4, -5])
m = minimo([-4, -5])
print('el mayor índice en el que se encuentra el elemento es: ', pos)
print(f'el elemento esta {rep} veces en la lista')
print(f'el máximo elemento de la lista es: {maxi}')
print(f'el minimo elemento de la lista es: {m}')