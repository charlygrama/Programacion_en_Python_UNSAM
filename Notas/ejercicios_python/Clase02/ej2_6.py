### Ejercicio 2.6: Transformar un script en una función
costo = 0
def costo_camion(costo_camion):
    
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Clase02/costo_camion.py', 'rt') as g:
        # headers = next(g)
        # for linea in g:
        #     fila = linea.split(',')
        #     precio = int(fila[1]) * float(fila[2])
        #     costo_total += precio
        #     print(costo_total)
        g.read()
        costo_total

costo_camion('../Data/camion.csv')
# costo = costo_camion('../Data/camion.csv')
# print('Costo total:', costo)

# costo_camion('Data/camion.csv')