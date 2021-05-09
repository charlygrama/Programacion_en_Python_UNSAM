# -*- coding: utf-8 -*-
### Ejercicio 7.4: De archivos a "objetos cual archivos"
# import csv
from pprint import pprint
def read_data(lines, select=None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se modifica el tipo de dato recuperado del ej 6.7
    '''
    encabezados = ['nombre', 'dia', 'hora', 'cajones', 'precio']
    for line in lines:
        # Lee los encabezados del archivo
        encabezados = next(lines)
    
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for line in lines:
            line[1] = int(line[1])
            if not line:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                line = [line[index] for index in indices]
    
            # Armar el diccionario
            registro = dict(zip(encabezados, line))
            
            registros.append(registro)

    return registros

lines = open('../Data/camion.csv', 'rt') 
data = read_data(lines, select = ['nombre', 'cajones']) 
# cajones_retenidos = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones'])
pprint(data)
