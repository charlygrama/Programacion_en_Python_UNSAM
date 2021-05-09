### Ejercicio 2.6: Transformar un script en una función
'''Computa el precio total del 
camion (cajones * precio) de un archivo'''
costo = 0
import csv
def costo_camion(costo_camion):
    costo_total = 0
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as f:
        lineas = csv.reader(f)
        headers = next(lineas)
        for linea in lineas:
            ncajones = int(linea[1])
            precio = float(linea[2]) 
            costo_total += ncajones * precio
    
    return costo_total

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
