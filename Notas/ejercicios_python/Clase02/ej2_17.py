### Ejercicio 2.17: Diccionarios como contenedores
import csv
from pprint import pprint
precios = {}
def leer_precios(precios):
    precios = {}
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as f:
        lineas = csv.reader(f)
        try:
            for linea in lineas:
                precios[linea[0]] = float(linea[1])
                items = [(lote)]
                precios = dict(items)
                print(precios)
        except IndexError:
            pass
    return precios                  
precios = leer_precios('../Data/precios.csv')
# precios['Naranja']