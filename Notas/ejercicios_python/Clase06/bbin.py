# -*- coding: utf-8 -*-
### Ejercicio 6.15: Insertar un elemento en una lista

def donde_insertar(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista, si no esta en la lista devuelve posicion donde se debería insertar'''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    if pos == -1:
        for i in lista:
            # pos = bisect.bisect(lista,i)
            # bisect.insort(lista, i)
            if lista[i-1] < x and lista[i+1] > x:
                lista.insert(i+1, x)
                pos = i+1 
                break
        print(x,'no encontrado')
        print('debe ser insertado en posición',pos,'para manetener lista ordenada')    
    else:
        print(x,'se encuntra en lista, en posición',pos) 
    return pos           
        
p = donde_insertar([0,1,2,4,5], 3)

