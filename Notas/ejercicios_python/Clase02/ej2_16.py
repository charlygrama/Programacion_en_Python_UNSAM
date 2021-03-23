### Ejercicio 2.16: Lista de diccionarios
import csv
lista = []
camion = {}
costo = 0.0
from pprint import pprint
def leer_camion(costo_camion):
    costo = 0.0
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as f:
        lineas = csv.reader(f)
        headers = next(lineas)
        
        for linea in lineas:
            lote = (linea[0]), int(linea[1]), float(linea[2])
            lista.append(lote)
            camion = dict(zip(headers, lote)) 

            nombre = linea[0]
            cajones = int(linea[1])
            precio = float(linea[2])
            costo += cajones * precio   

            print(camion)
            # print(costo)

    return camion, costo

camion, costo = leer_camion('../Data/camion.csv')
print('\nse paga al productor: ',costo)