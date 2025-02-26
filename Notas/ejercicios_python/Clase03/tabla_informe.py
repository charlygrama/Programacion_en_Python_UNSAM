### Ejercicio 3.13: Recolectar datos
import csv
from pprint import pprint
camion = {}
lista = []
costo = 0.0
ventas = 0.0
ganancia = 0.0

def leer_camion(camion):
    lista_camion = []
    with open('../Data/camion.csv', 'rt') as c:
        lineas = csv.reader(c)
        next(lineas)
        for linea in lineas:
            nombre = linea[0]
            cajones = int(linea[1])
            precio = float(linea[2])
            dicc_camion = {'nombre': nombre, 'cajones' : cajones, 'precio' : precio}
            lista_camion.append(dicc_camion)
    return lista_camion

def leer_precios(precios):
    dicc_precios = {}
    with open('../Data/precios.csv', 'rt') as p:
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
    with open('../Data/precios.csv', 'rt') as f:
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

def hacer_informe(camion, precios):
    lista = []
    for d in camion:
        if d['nombre'] in precios:
            dif = (precios[d['nombre']] - float(d['precio']))
            t = (d['nombre'], int(d['cajones']), float(d['precio']), dif)
            lista.append(t)
    return lista


print('-'*45)

path_camion = '../Data/camion.csv'
path_precios_venta = '../Data/precios.csv'

camion = leer_camion(path_camion)
precios = leer_precios(path_precios_venta)
informe = hacer_informe(camion, precios)
for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
print('-'*45)



