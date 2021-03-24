### Ejercicio 2.2: Lectura de un archivo de datos
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

costo = costo_camion('../Data/camion.csv')
print('El costo del camión es: ', costo)