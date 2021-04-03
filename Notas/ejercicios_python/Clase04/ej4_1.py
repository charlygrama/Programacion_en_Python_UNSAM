# -*- coding: utf-8 -*-

### Ejercicio 4.1: Debugger

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i=len(lista)
    while i > 0:    # tomo el último elemento
        i=i-1
        invertida.append (lista.pop(i))  # la función modifica el valor de la lista de entrada

l = [1, 2, 3, 4, 5]
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')