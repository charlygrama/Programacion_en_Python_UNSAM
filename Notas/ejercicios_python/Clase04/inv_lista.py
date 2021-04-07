# -*- coding: utf-8 -*-
### Ejercicio 4.8: Invertir una lista

def invertir_lista(lista):
    for e in lista: # Recorro la lista
        invertida = []
        invertida = lista[::-1] #agrego el elemento e al principio de la lista invertida

    return invertida

# lista = invertir_lista([1, 2, 3, 4, 5])
lista = invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
print(lista)


