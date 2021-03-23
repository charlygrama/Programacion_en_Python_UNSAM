# informe.py

# informe.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/04_Contenedores.md#ejercicio-215-lista-de-tuplas

# Ejercicio 2.15

# El archivo Data/camion.csv contiene la lista de cajones cargados en un camión. En el Ejercicio 2.6 de la sección anterior 
# escribiste una función costo_camion(nombre_archivo) que leía el archivo y realizaba un cálculo.
# 
# La función debería verse parecida a ésta:
# 
# # fragmento de costo_camion.py
# import csv
# ...
# 
# def costo_camion(nombre_archivo):
#     '''Computa el precio total del camion (cajones * precio) de un archivo'''
#     total = 0.0
# 
#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             ncajones = int(row[1])
#             precio = float(row[2])
#             total += ncajones * precio
#     return total
# 
# ...
# 
# Usando este código como guía, creá un nuevo archivo informe.py. En este archivo, definí una función leer_camion(nombre_archivo) 
# que abre un archivo con el contenido de un camión, lo lee y devuelve la información como una lista de tuplas. 
# Para hacerlo vas a tener que hacer algunas modificaciones menores al código de arriba.
# 
# Primero, en vez de definir total = 0, tenés que empezar con una variable que empieza siendo una lista vacía Por ejemplo:
# 
# camion = []
# 
# Después, en vez de sumar el costo, tenés que pasar cada fila a una tupla igual a como lo hiciste en el último ejercicio, y agregarla a la lista. Por ejemplo:
# 
# for row in rows:
#     lote = (row[0], int(row[1]), float(row[2]))
#     camion.append(lote)
# 
# Por último, la función debe devolver la lista camion.
# 
# Experimentá con tu función interactivamente (acordate de que primero tenés que correr el programa informe.py en el intérprete):
# 
# Ayuda: Usá -i para ejecutar un archivo en la terminal y quedar en el intérprete
# 
# >>> camion = leer_camion('../Data/camion.csv')
# >>> camion
# [('Lima', 100, 32.2), ('Naranja', 50, 91.1), ('Limon', 150, 83.44), ('Mandarina', 200, 51.23),('Durazno', 95, 40.37), 
# ('Mandarina', 50, 65.1), ('Naranja', 100, 70.44)]
# >>>
# >>> camion[0]
# ('Lima', 100, 32.2)
# >>> camion[1]
# ('Naranja', 50, 91.1)
# >>> camion[1][1]
# 50
# >>> total = 0.0
# >>> for s in camion:
#         total += s[1] * s[2]
# 
# >>> print(total)
# 47671.15
# >>>
# 
# Esta lista de tuplas que creaste es muy similar a un array o matriz bidimensional. Por ejemplo, podés acceder a una fila 
# específica y columna específica usando una búsqueda como camion[fila][columna] donde fila y columna son números enteros.
# 
# También podés reescribir el último ciclo for usando un comando como éste:
# 
# >>> total = 0.0
# >>> for nombre, cajones, precio in camion:
#             total += cajones*precio
# 
# >>> print(total)
# 47671.15
# >>>
# 
# Observación: la instrucción += es una abreviación. Poner a += b es equivalente a poner a = a + b



# import csv
# 
# def leer_camion(nombre_archivo):
#     tupla_camion = []
#     with open(nombre_archivo, 'rt') as raw_file:
#         csv_content = csv.reader(raw_file)
#         next(csv_content)
#         for item in csv_content:
#             nombre = item[0]
#             numero_cajones = int(item[1])
#             precio = float(item[2])
#             tupla_item = (nombre, numero_cajones, precio)
#             tupla_camion.append(tupla_item)
#     return tupla_camion
# 
# camion = leer_camion('../Data/camion.csv')



# Output:
# 
# >>> camion
# [('Lima', 100, 32.2), ('Naranja', 50, 91.1), ('Caqui', 150, 103.44), ('Mandarina', 200, 51.23), ('Durazno', 95, 40.37), ('Mandarina', 50, 65.1), ('Naranja', 100, 70.44)]


######################

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/04_Contenedores.md#ejercicio-216-lista-de-diccionarios

# Ejercicio 2.16

# Tomá la función que escribiste en el ejercicio anterior y modificala para representar cada cajón del 
# camión con un diccionario en vez de una tupla. En este diccionario usá los campos "nombre", "cajones" y "precio" 
# para representar las diferentes columnas del archivo de entrada.
# 
# Experimentá con esta función nueva igual que en el ejercicio anterior.
# 
# >>> camion = leer_camion('../Data/camion.csv')
# >>> camion
# [{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Limon', 
# 'cajones': 150, 'precio': 83.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 
# 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]
# >>> camion[0]
# {'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}
# >>> camion[1]
# {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}
# >>> camion[1]['cajones']
# 50
# >>> total = 0.0
# >>> for s in camion:
#         total += s['cajones']*s['precio']
# 
# >>> print(total)
# 47671.15
# >>>
# 
# Fijate que acá los distintos campos para cada entrada se acceden a través de claves en vez de la posición en la lista. 
# Muchas veces preferimos esto porque el código resulta más fácil de leer. Tanto para otres como para nosotres en el futuro.
# 
# Mirar diccionarios y listas muy grandes puede ser un lío. Para limpiar el output para debuguear, probá la función pprint 
# (Pretty-print) que le da un formato más sencillo de interpretar.
# 
# >>> from pprint import pprint
# >>> pprint(camion)
# [{'nombre': 'Lima', 'precio': 32.2, 'cajones': 100},
#     {'nombre': 'Naranja', 'precio': 91.1, 'cajones': 50},
#     {'nombre': 'Limon', 'precio': 83.44, 'cajones': 150},
#     {'nombre': 'Mandarina', 'precio': 51.23, 'cajones': 200},
#     {'nombre': 'Durazno', 'precio': 40.37, 'cajones': 95},
#     {'nombre': 'Mandarina', 'precio': 65.1, 'cajones': 50},
#     {'nombre': 'Naranja', 'precio': 70.44, 'cajones': 100}]
# >>>

# import csv
# from pprint import pprint
# 
# def leer_camion(nombre_archivo):
#     diccionario_camion = []
#     with open(nombre_archivo, 'rt') as raw_file:
#         csv_content = csv.reader(raw_file)
#         next(csv_content)
#         for item in csv_content:
#             nombre = item[0]
#             numero_cajones = int(item[1])
#             precio = float(item[2])
#             diccionario_item = {"nombre": nombre, "precio": precio, "cajones": numero_cajones}
#             diccionario_camion.append(diccionario_item)
#     return diccionario_camion
# 
# camion = leer_camion('../Data/camion.csv')
# 
# total = 0
# for item in camion:
#     total += item["cajones"] * item["precio"]
# 
# print(total)
# 
# # Output: 
# 
# # >>> print(total)
# # 47671.15
# 
# pprint(camion)
# 
# # Output:
# 
# # >>> pprint(camion)
# # [{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
# #  {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
# #  {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
# #  {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
# #  {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
# #  {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
# #  {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]

 
######################

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/04_Contenedores.md#ejercicio-217-diccionarios-como-contenedores

# Ejercicio 2.17

# Los diccionarios son útiles si querés buscar elementos usando índices que no sean números enteros. En la terminal de Python, jugá con un diccionario:
# 
# >>> precios = {}
# >>> precios['Naranja'] = 92.45
# >>> precios['Mandarina'] = 45.12
# >>> precios
# ... mirá el resultado ...
# >>> precios['Naranja']
# 92.45
# >>> precios['Manzana']
# ... mirá el resultado ...
# >>> 'Manzana' in precios
# False
# >>>
# 
# En el Ejercicio 2.7 escribiste una función que busca el precio de una determinada fruta o verdura en el archivo 
# ../Data/precios.csv. Esto es útil para saber sobre un producto en particular, pero si necesitás tener los precios 
# de toda la mercadería, no resulta práctico abrir y cerrar el archivo para consultar cada precio. Por eso ahora te 
# proponemos generar un diccionario que contenga todos los precios. En este diccionario, podés consultar luego los precios de cada producto.
# 
# Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto de precios como éste arme un diccionario 
# donde las claves sean los nombres de frutas y verduras, y los valores sean los precios por cajón.
# 
# Para hacerlo, empezá con un diccionario vacío y andá agregándole valores igual a como hiciste antes, pero ahora esos 
# valores los vas leyendo del archivo.
# 
# Vamos a usar esta estructura de datos para buscar rápidamente los precios de las frutas y verduras.
# 
# Un par de consejos: Usá el módulo csv igual que antes.
# 
# >>> import csv
# >>> f = open('../Data/precios.csv', 'r')
# >>> rows = csv.reader(f)
# >>> for row in rows:
#         print(row)
# 
# 
# ['Lima', '40.22']
# ['Uva', '24.85']
# ...
# []
# >>>
# 
# El archivo Data/precios.csv puede tener líneas en blanco, esto te puede traer complicaciones. Observá que arriba figura 
# una lista vacía (la última), porque la última línea del archivo no tenía datos.
# 
# Puede suceder que esto haga que tu programa termine con una excepción. Usá los comandos try y except para evitar el problema. 
# Para pensar: ¿Sería mejor prevenir estos problemas con el comando if en vez de try y except?
# 
# Una vez que hayas escrito tu función leer_precios(), testeala interactivamente para asegurarte de que funciona bien:
# 
# >>> precios = leer_precios('../Data/precios.csv')
# >>> precios['Naranja']
# 106.28
# >>> precios['Mandarina']
# 80.89
# >>>

# import csv
# from pprint import pprint
#  
# def leer_camion(nombre_archivo):
#     diccionario_camion = []
#     with open(nombre_archivo, 'rt') as raw_file:
#         csv_content = csv.reader(raw_file)
#         next(csv_content)
#         for item in csv_content:
#              nombre = item[0]
#              numero_cajones = int(item[1])
#              precio = float(item[2])
#              diccionario_item = {"nombre": nombre, "precio": precio, "cajones": numero_cajones}
#              diccionario_camion.append(diccionario_item)
#     return diccionario_camion
# 
# def leer_precios(nombre_archivo):
#     diccionario_precios = {}
#     with open(nombre_archivo, "rt") as csv_file:
#         csv_content = csv.reader(csv_file)
#         for item in csv_content:
#             try:
#                 nombre = item[0]
#                 precio = float(item[1])
#                 diccionario_precios[nombre] = precio
#             except:
#                 continue
#     return diccionario_precios
# 
# 
# precios_leidos = leer_precios('../Data/precios.csv')

######################


# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/04_Contenedores.md#ejercicio-218-balances

# Ejercicio 2.18

# Supongamos que los precios en camion.csv son los precios pagados al productor de frutas 
# mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.
# 
# Ahora vamos calcular el balance del negocio: juntá todo el trabajo que hiciste recién en tu programa informe.py 
# (usando las funciones leer_camion() y leer_precios()) y completá el programa para que con los precios del camión 
# (Ejercicio 2.16) y los de venta en el negocio (Ejercicio 2.17) calcule lo que costó el camión, lo que se recaudó 
# con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

import csv
from pprint import pprint
 
def leer_camion(nombre_archivo):
    diccionario_camion = []
    with open(nombre_archivo, 'rt', encoding="utf-8") as raw_file:
        csv_content = csv.reader(raw_file)
        next(csv_content)
        for item in csv_content:
             nombre = item[0]
             numero_cajones = int(item[1])
             precio = float(item[2])
             diccionario_item = {"nombre": nombre, "precio": precio, "cajones": numero_cajones}
             diccionario_camion.append(diccionario_item)
    return diccionario_camion

def leer_precios(nombre_archivo):
    diccionario_precios = {}
    with open(nombre_archivo, "rt", encoding="utf-8") as csv_file:
        csv_content = csv.reader(csv_file)
        for item in csv_content:
            try:
                nombre = item[0]
                precio = float(item[1])
                diccionario_precios[nombre] = precio
            except:
                continue
    return diccionario_precios

def costo_camion(csv_file):
    costo_total = 0
    raw_file = open(csv_file, "r")
    file_content = csv.reader(raw_file)
    next(file_content) # Remove first item of csv, that will remove the headers
    for item in file_content:
        cajones_item = int(item[1])
        precio_item = float(item[2])
        costo_total += cajones_item * precio_item
    raw_file.close()
    return costo_total

def buscar_precio(fruta):
    precio = 0
    with open('../Data/precios.csv', 'r') as csv_file:
        csv_content = csv.reader(csv_file)
        for item in csv_content:
            nombre_csv = item[0]
            precio_csv = item[1]
            if nombre_csv == fruta:
                precio = precio_csv
        return float(precio)


path_camion = '../Data/camion.csv'
path_precios_venta = '../Data/precios.csv'

camion = leer_camion(path_camion)

costo_de_camion = costo_camion(path_camion)

recaudacion = 0
for producto in camion:
    recaudacion += buscar_precio(producto["nombre"]) * producto["cajones"]


diferencia = recaudacion - costo_de_camion

mensaje = f"Costo de Camion: {costo_de_camion} | Recaudacion: {recaudacion} | Ganancia: {diferencia:.2f}"

print(mensaje)