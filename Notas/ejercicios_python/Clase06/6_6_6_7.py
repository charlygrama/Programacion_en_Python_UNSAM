# -*- coding: utf-8 -*-
### Ejercicio 6.6: Parsear un archivo CSV
import csv
from pprint import pprint

def parse_csv(camion):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open('../Data/camion.csv', 'rt') as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros

camion = parse_csv('../Data/camion.csv')
pprint(camion)

#%%
### Ejercicio 6.7: Selector de Columnas
# import csv

def parse_csv(camion):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    encabezados = ['nombre', 'dia', 'hora', 'cajones', 'precio']
    select = ['nombre', 'cajones']
    with open('../Data/camion.csv', 'rt') as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

cajones_retenidos = parse_csv('../Data/camion.csv')
pprint(cajones_retenidos)