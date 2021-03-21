### Ejercicio 2.14: Diccionario geringoso.
def diccionario_geringoso(l1):
    l2 = []
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
    
    dicc_de_listas = {}
    
    for i in range(len(l1)):
        dicc_de_listas[ l1[i] ] = l2[i]
    print(dicc_de_listas)

lista = ['banana', 'manzana', 'mandarina']
diccionario_geringoso(lista)