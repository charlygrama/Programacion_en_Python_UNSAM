### Ejercicio 2.14: Diccionario geringoso.
def diccionario_geringoso(capadepenapa):
    cadena = 'Geringoso'
    # capadepenapa = ''

    for c in cadena:
        if c in 'aeiou':
            capadepenapa += c + 'p' + c
        else:
            capadepenapa += c
    print(capadepenapa)

lista = ['banana', 'manzana', 'mandarina']
diccionario_geringoso(lista)