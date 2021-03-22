### Ejercicio 2.14: Diccionario geringoso.
# https://www.delftstack.com/es/howto/python/python-convert-list-into-dictionary/ link para metodo zip
def diccionario_geringoso(l1):
    l2 = []
    
    for c in range(0, len(l1)):
        capadepenapa = '' 
        for c in l1[c]:
            if c in 'aeiou':
                capadepenapa += c + 'p' + c
            else:
                capadepenapa += c

        l2.append(capadepenapa)
    
    dict_from_list = dict(zip(lista, l2)) 
    print(dict_from_list)

lista = ['banana', 'manzana', 'mandarina']
diccionario_geringoso(lista)