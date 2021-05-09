# -*- coding: utf-8 -*-
### Ejercicio 4.9: Propagación
# Escribí una función llamada `propagar` que reciba un vector con 0's, 1's y -1's y devuelva un vector en el que los 1's se propagaron a sus vecinos con 0. Guardalo en un archivo `propaga.py`.
# 0 (nuevo), un 1 (encendido) o un -1 (carbonizado).

def propagar(fosforos):
    n = len(fosforos)
    for i in range(n-1):
        if (fosforos[i] == 1) and (fosforos[i+1] == 0):
            fosforos[i+1] = 1
    return fosforos

fosforos = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
print(fosforos)
f = propagar(fosforos)
print(f)

'''python
>>> propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
              [ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
>>> propagar([ 0, 0, 0, 1, 0, 0])
            [ 1, 1, 1, 1, 1, 1]'''