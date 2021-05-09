# Ejercicio 3.9: La función zip()
import csv
from pprint import pprint
camion = {}
lista = []
costo = 0.0

def leer_camion(camion):
    costo = 0.0
    lista_camion = []
    with open('../Data/fecha_camion.csv', 'rt') as c:
        filas = csv.reader(c)
        encabezados= next(filas)
        for n_fila, fila in enumerate(filas, start = 1):
            record = dict(zip(encabezados, fila))
            print(record)
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return lista_camion

def costo_camion(costo_camion):
    costo = 0.0
    with open('../Data/fecha_camion.csv', 'rt') as c:
        filas = csv.reader(c)
        encabezados= next(filas)
        for n_fila, fila in enumerate(filas, start = 1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo

print('-----------------------------------------------------------------------------------------------------------------------')

path_camion = '../Data/fecha_camion.csv'

camion = leer_camion(path_camion)
costo = costo_camion(path_camion)

print('-----------------------------------------------------------------------------------------------------------------------')
print('El costo del camion fue: {0} '.format(costo))
print('-----------------------------------------------------------------------------------------------------------------------')
