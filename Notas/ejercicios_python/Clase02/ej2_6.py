### Ejercicio 2.6: Transformar un script en una función
costo = 0
def costo_camion(costo_camion):
    
    costo_total = 0
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as f:
        headers = next(f)
        for linea in f:
            fila = linea.split(',')
            precio = int(fila[1]) * float(fila[2])
            costo_total += precio
    
    return costo_total

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
