# -*- coding: utf-8 -*-
### Ejercicio 6.8: Conversión de tipo
import csv
from pprint import pprint

def parse_csv(camion, select = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se modifica el tipo de dato recuperado del ej 6.7
    '''
    encabezados = ['nombre', 'dia', 'hora', 'cajones', 'precio']
    
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
            fila[1] = int(fila[1])
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            
            registros.append(registro)

    return registros

cajones_retenidos = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones'])
pprint(cajones_retenidos)