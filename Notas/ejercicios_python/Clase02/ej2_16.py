### Ejercicio 2.16: Lista de diccionarios
import csv
t = []
camion = {}
from pprint import pprint
def leer_camion(costo_camion):
    # costo = 0.0
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as f:
        lineas = csv.reader(f)
        headers = next(lineas)
        
        for linea in lineas:
            lote = (linea[0]), int(linea[1]), float(linea[2])
            t.append(lote)
            camion = dict(zip(headers, lote)) 
            print(camion)
    return camion

camion = leer_camion('../Data/camion.csv')


           