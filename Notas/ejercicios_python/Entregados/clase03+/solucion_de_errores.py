#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era que la función no recorria la expresion y returnaba el valor muy pronto.
#    Lo corregí :
            # * haciendo que la funcion recorra la epresion y retorne True si encuentra una 'a'.
            # * gardando en una variable cuando el valor de False para q continue recorriendo la expresion.
            # * cuando termina de recorrer la expresion retorna el valor.
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            a = False
        i += 1
    return a
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2: Sintaxis
#Comentario: El error es que las palabras del código estaban mal escritas
#    Lo corregí :
            # * definiendo bien las funciones agregando ':'
            # * agregando '==' en el if
            # * cambiando el Falso por False
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.3: Tipos
#Comentario: El error es que tiene_uno(1984) pasa como parámetro un dato de tipo 'int' y no se puede aplicar el metodo len, además cuando encuentra una 'a'
# sigue recorriendo la expresion
#    Lo corregí :
            # * agregando ' ' a tiene_uno(1984) para que pase como parámetro str
            # * cuando encuentre una 'a' que retorne True
            # * cambiando el Falso por False
#    A continuación va el código corregido

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            return True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')

#%%
# Ejercicio 3.4: Alcances
#Comentario: El error es que suma(a,b) devolvia 'none' ya que c no estaba definida y 'a' y 'b' estaban definidas globalmente y
# en la funcion sobreescribiendo sus valores
#    Lo corregí :
            # * agregando un return a la funcion y eliminando c dentro de la funcion
#    A continuación va el código corregido


def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
# Ejercicio 3.5: Pisando memoria
#Comentario: El error era que se hacia referencia a una ubicacion incorrecta de camion.csv
#    Lo corregí :
            # * modificando la refereencia a ubicacion del archivo
#    A continuación va el código corregido

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open('../Data/camion.csv',"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)