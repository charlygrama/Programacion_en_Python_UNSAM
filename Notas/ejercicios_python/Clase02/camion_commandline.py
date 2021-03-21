### Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros
import csv
import sys
costo = 0
def costo_camion(costo_camion):
    costo_total = 0
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as f:
        lineas = csv.reader(f)
        headers = next(lineas)
        for linea in lineas:
            precio = int(linea[1]) * float(linea[2])
            costo_total += precio

    if len(sys.argv) == 2:
        camion_commandline = sys.argv[1]
    else:
        camion_commandline = '../Data/camion.csv'

    return costo_total

costo = costo_camion('camion_commandline')
print('Costo total:', costo)