exitr# -*- coding: utf-8 -*-
### Ejercicio 6.12: Un poco más allá
import csv
camion = {}
lista = []
# costo = 0.0
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

def imprimir_informe(informe):
     print('-'*50)
     print('     nombre',' ','  cajones',' ', ' precio',' ', '   cambio')
     print('-'*50)
     for nombre, cajones, precio, cambio in informe:
            print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
            # print('-'*50)
            
# def informe_camion('../Data/camion.csv', '../Data/precios.csv'):    
    
camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)
informe = imprimir_informe(informe)


def costo_camion(costo_camion):
    costo = 0.0
    with open('../Data/camion.csv', 'rt') as c:
        lineas = csv.reader(c)
        next(lineas)
        for linea in lineas:
            cajones = int(linea[1])
            precio = float(linea[2])
            costo += cajones * precio 
    return costo

print()
costo = costo_camion('../Data/camion.csv')
print('El costo del camión es: ', costo)