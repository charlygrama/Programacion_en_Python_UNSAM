### Ejercicio 2.14: Diccionario geringoso.
def diccionario_geringoso():
    cadena = 'Geringoso'
    capadepenapa = ''

    for c in cadena:
        if c in 'aeiou':
            capadepenapa += c + 'p' + c
        else:
            capadepenapa += c
    return capadepenapa

diccionario_geringoso()