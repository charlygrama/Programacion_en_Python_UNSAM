### Ejercicio 2.14: Diccionario geringoso.
def diccionario_geringoso(l1):
    l2 = []
    # t = ('', '', '')
    d = { 
        lista[0] : '', 
        lista[1] : '', 
        lista[2] : '' 
    }
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