### Ejercicio 2.15: Lista de tuplas
import csv
from pprint import pprint
camion = {}
d_precios = {}
costo = 0.0
lista = []

def leer_camion(camion):
    lista_camion = []
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as c:
        lineas = csv.reader(c)
        next(lineas)
        for linea in lineas:
            nombre = linea[0] 
            cajones = int(linea[1])
            precio = float(linea[2])
            dicc_camion = {'nombre': nombre, 'precio' : precio, 'cajones' : cajones}
            lista_camion.append(dicc_camion)
    return dicc_camion

def costo_camion(costo_camion):
    costo = 0.0
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/camion.csv', 'rt') as c:
        lineas = csv.reader(c)
        next(lineas)
        for linea in lineas:
            cajones = int(linea[1])
            precio = float(linea[2])
            costo += cajones * precio 
    return costo

def leer_precios(precios):
    dicc_precios = {}  
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as p:    
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
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as f:
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

print('-------------------------------------------------------------------------')

camion = leer_camion('../Data/camion.csv') 
costo = costo_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
# print(precios['Naranja'])
# buscar_precio('Papa')


print('-------------------------------------------------------------------------')
ventas = 0
for fruto in camion:
    ventas += buscar_precio(fruto['nombre']) * fruto['cajones']

ganancia = ventas - costo

mostrar = f'Costo de Camion: {costo} | Ventas: {ventas} | Ganancia: {ganancia}' 
print(mostrar)  




