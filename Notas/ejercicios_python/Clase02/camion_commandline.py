### Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros
import csv
import sys
import csv
def costo_camion(costo_camion):
    costo = 0.0
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as c:
        lineas = csv.reader(c)
        next(lineas)
        for linea in lineas:
            cajones = int(linea[1])
            precio = float(linea[2])
            costo += cajones * precio 
    return costo

if len(sys.argv) == 2:
    camion_commandline = sys.argv[1]
else:
    camion_commandline = '../Data/camion.csv'

costo = costo_camion('camion_commandline')
print('El costo del camión es: ', costo)