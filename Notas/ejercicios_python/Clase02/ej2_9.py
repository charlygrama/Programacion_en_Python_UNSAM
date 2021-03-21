### Ejercicio 2.9: Funciones de la biblioteca
import csv
costo_total = 0
with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as f:
    lineas = csv.reader(f)
    headers = next(lineas)
    for linea in lineas:
        precio = int(linea[1]) * float(linea[2])
        costo_total += precio
    print(costo_total)