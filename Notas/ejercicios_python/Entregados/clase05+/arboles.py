# -*- coding: utf-8 -*-
# %%
# Ejercicio 4.18: Lectura de todos los árboles

import matplotlib.pyplot as plt
import os
import csv

def leer_arboles(archivo):
    arboleda = []
    with open('../Data/arbolado.csv', 'rt', errors='ignore', encoding='utf-8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            record = dict(zip(encabezado, fila))
            arboleda.append(record)
    return arboleda

arboleda = leer_arboles('../Data/arbolado.csv')
# conjunto = especies(archivo)
print('-'*65)
# print(arboleda)
print('-'*65)

# %%
# Ejercicio 4.19: Lista de altos de Jacarandá
# Ejercicio 5.24: Histograma de altos de Jacarandás


def altura(arboleda):
    H = [float(arbol['altura_tot']) for arbol in arboleda]
    # print(H)
    return H

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')

arboleda = leer_arboles('../Data/arbolado.csv')

altos = altura(arboleda)
plt.ylabel("cantidad")
plt.xlabel("altura (m)")
plt.title("altura Jacarandás")
plt.hist(altos, bins='auto')
# %%
# Ejercicio 4.20: Lista de altos y diámetros de Jacarandá
# Ejercicio 5.25: Scatterplot (diámetro vs alto) de Jacarandás


def DyH(arboleda):
    lista_altura = []
    lista_diametro = []
    # HD =[ (arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá' ]
    H = [(arbol['altura_tot'])
         for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    lista_altura.append(H)

    D = [(arbol['diametro'])
         for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

    lista_diametro.append(D)

    return lista_diametro, lista_altura


arboleda = leer_arboles('../Data/arbolado.csv')

d, h = DyH(arboleda)
plt.scatter(d,h, alpha=0.5)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
# %%
