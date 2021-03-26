# Ejercicio 3.9: La función zip()
import csv
from pprint import pprint
camion = {}
lista = []
costo = 0.0
# ventas = 0.0
# ganancia = 0.0


def leer_camion(camion):
    costo = 0.0
    lista_camion = []
    with open('../python_UNSAM/Notas/ejercicios_python/Data/fecha_camion.csv', 'rt') as c:
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
    with open('../python_UNSAM/Notas/ejercicios_python/Data/fecha_camion.csv', 'rt') as c:
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

# def leer_precios(precios):
#     dicc_precios = {}  
#     with open('../python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as p:    
#         lineas = csv.reader(p)
#         for linea in lineas:
#             try:
#                 nombre = linea[0] 
#                 precio = float(linea[1])
#                 dicc_precios[nombre] = precio
#             except IndexError:
#                 pass
#     return dicc_precios          

# def buscar_precio(fruta):
#     precio_fruta = 0
#     with open('../python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as f:
#         lineas = csv.reader(f)
#         for linea in lineas:
#             try:
#                 nombre = linea[0]
#                 precio = linea[1] 
#                 if nombre == fruta:
#                     precio_fruta = precio
#                     print(precio_fruta)
#             except IndexError:
#                 pass
#     return float(precio_fruta)

print('-----------------------------------------------------------------------------------------------------------------------')

path_camion = '../Data/fecha_camion.csv'
# path_precios_venta = '../Data/precios.csv'

camion = leer_camion(path_camion) 
costo = costo_camion(path_camion)
# precios = leer_precios(path_precios_venta)
# print(precios['Naranja'])
# buscar_precio('Papa')

# for producto in precios:
#     for p in camion:
#         if producto in p['nombre']:
#             ventas += precios[producto] * p['cajones']

# ganancia = ventas - costo

print('-----------------------------------------------------------------------------------------------------------------------')
print('El costo del camion fue: {0} '.format(costo))
print('-----------------------------------------------------------------------------------------------------------------------')
