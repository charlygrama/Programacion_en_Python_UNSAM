### Ejercicio 2.17: Diccionarios como contenedores
import csv
from pprint import pprint
costo = 0.0
d_precios = {}
def leer_precios(precios):
    d_precios = {}
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as f:
        lineas = csv.reader(f)
        try:
            for linea in lineas:
                lote = linea[0], float(linea[1])
                items = [(lote)]
                d_precios = dict(items)
                print(d_precios)
        except IndexError:
            pass
    return precios                  

precios = leer_precios('../Data/precios.csv')
