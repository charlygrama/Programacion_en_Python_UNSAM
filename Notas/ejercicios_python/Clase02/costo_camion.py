### Ejercicio 2.2: Lectura de un archivo de datos
costo_total = 0
with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as f:
    headers = next(f)
    for linea in f:
        fila = linea.split(',')
        precio = int(fila[1]) * float(fila[2])
        costo_total += precio
    print(costo_total)