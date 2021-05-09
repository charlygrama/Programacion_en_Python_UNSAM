# Ejercicio 3.8: Un ejemplo práctico de enumerate()
import csv
costo = {}
from pprint import pprint
def costo_camion(costo_camion):
    with open('../Data/camion.csv', 'rt') as f:
        lineas = csv.reader(f)
        for n_fila, fila in enumerate(lineas, start = 1):
            print(n_fila, fila)
            try:
                fila[0]
                int(fila[1])
                float(fila[2])
            except ValueError:
                print('------------------------------------------------------------------')
                print(f'Fila {n_fila}: No pude interpretar: {fila}') 
                print('------------------------------------------------------------------')
    return lineas

costo = costo_camion('../Data/camion.csv')
