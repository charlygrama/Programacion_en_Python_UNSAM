#%%
### Ejercicio 4.18: Lectura de todos los árboles
# escribí otra `leer_arboles(nombre_archivo)` que lea el archivo indicado y devuelva una **lista de diccionarios** con la información de todos los árboles en el archivo. La función debe devolver una lista conteniendo un diccionario por cada árbol con todos los datos.
# Vamos a llamar `arboleda` a esta lista.
import csv
from pprint import pprint
def leer_arboles(archivo):
    arboleda = []
    with open('../Data/arbolado.csv', 'rt', errors = 'ignore', encoding = 'utf-8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            record = dict(zip(encabezado, fila))
            arboleda.append(record)
    return arboleda


arboleda = leer_arboles('../Data/arbolado.csv')
# conjunto = especies(archivo)
print('-'*65)
pprint(arboleda)
print('-'*65)

#%%
### Ejercicio 4.19: Lista de altos de Jacarandá
# Usando comprensión de listas y la variable `arboleda` podés por ejemplo armar la lista de la altura de los árboles.

H = [float(arbol['altura_tot']) for arbol in arboleda]
pprint(H)

#%%
### Ejercicio 4.20: Lista de altos y diámetros de Jacarandá
# En el ejercicio anterior usaste una sola linea para seleccionar las alturas de los Jacarandás en parques porteños. Ahora te proponemos que armes una nueva lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto sino también el diámetro de cada Jacarandá en la lista.

HD =[ (arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá' ]

pprint(HD)


#%%