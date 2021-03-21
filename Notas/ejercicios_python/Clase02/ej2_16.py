### Ejercicio 2.16: Lista de diccionarios
costo = 0
camion = []
import csv
from pprint import pprint
def leer_camion(costo_camion):
    costo_total = 0
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as f:
        lineas = csv.reader(f)
        headers = next(lineas)
        for linea in lineas:
            lote = ((linea[0]), int(linea[1]), float(linea[2]))
            ncajones = int(linea[1])
            precio = float(linea[2])
            camion.append(lote)
            costo_total += ncajones * precio
    
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)