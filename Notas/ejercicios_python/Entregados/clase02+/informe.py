### Ejercicio 2.15: Lista de tuplas
import csv
from pprint import pprint
camion = {}
lista = []
costo = 0.0
ventas = 0.0
ganancia = 0.0

def leer_camion(camion):
    lista_camion = []
    with open('../python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as c:
        lineas = csv.reader(c)
        next(lineas)
        for linea in lineas:
            nombre = linea[0] 
            cajones = int(linea[1])
            precio = float(linea[2])
            dicc_camion = {'nombre': nombre, 'cajones' : cajones, 'precio' : precio}
            lista_camion.append(dicc_camion)
    return lista_camion

def costo_camion(costo_camion):
    costo = 0.0
    with open('../python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as c:
        lineas = csv.reader(c)
        next(lineas)
        for linea in lineas:
            cajones = int(linea[1])
            precio = float(linea[2])
            costo += cajones * precio 
    return costo

def leer_precios(precios):
    dicc_precios = {}  
    with open('../python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as p:    
        lineas = csv.reader(p)
        for linea in lineas:
            try:
                nombre = linea[0] 
                precio = float(linea[1])
                dicc_precios[nombre] = precio
            except IndexError:
                pass
    return dicc_precios          

def buscar_precio(fruta):
    precio_fruta = 0
    with open('../python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as f:
        lineas = csv.reader(f)
        for linea in lineas:
            try:
                nombre = linea[0]
                precio = linea[1] 
                if nombre == fruta:
                    precio_fruta = precio
                    print(precio_fruta)
            except IndexError:
                pass
    return float(precio_fruta)

print('-----------------------------------------------------------------------------------------------------------------------')
camion = leer_camion('../Data/camion.csv') 
costo = costo_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
# print(precios['Naranja'])
# buscar_precio('Papa')

for producto in precios:
    for p in camion:
        if producto in p['nombre']:
            ventas += precios[producto] * p['cajones']

ganancia = ventas - costo
print('El costo del camion fue: {0} | Las ventas fueron: {1} | La ganancia obtenida fue {2} '.format(costo, ventas, format(ganancia, '0.2f')))
print('-----------------------------------------------------------------------------------------------------------------------')
