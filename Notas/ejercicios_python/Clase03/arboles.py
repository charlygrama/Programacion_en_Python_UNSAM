### Ejercicio 3.18: Lectura de los árboles de un parque
import csv
from pprint import pprint

def leer_parque(archivo, parque):
    cantidad = 0
    lista_arboles = []
    with open('../Data/arbolado.csv', 'rt', errors = 'ignore', encoding = 'utf-8') as f:
        filas = csv.reader(f)
        encabezado= next(filas)
        for fila in filas:
            record = dict(zip(encabezado, fila))
            if record['espacio_ve'] == parque:
                cantidad += 1
                lista_arboles.append(record)
    return lista_arboles

archivo = leer_parque('../Data/arbolado.csv', 'GENERAL PAZ')
print(archivo)