# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:13:41 2021

@author: carlos
"""

### Ejercicio 5.1: Generala servida

# Escribí una función `tirar()` que devuelva una lista con cinco dados generados aleatoriamente. .
import random

lista = []
def tirar():
    for i in range(5):
        lista.append(random.randint(1,6))
    return lista

dados = tirar() 
print(dados)
#%%
# Escribí otra función llamada `es_generala(tirada)` que devuelve `True` si y sólo si los cinco dados de la lista `tirada` son iguales
lista = []
def tirada():
    for i in range(5):
        lista.append(random.randint(1,6))
    return lista

cond = True
def es_generala(tirada):
    for p, t in enumerate(tirada) :
        if t == 6:
            cond = True
        else:
            break
    cond = False
    return cond

dados = tirada()
generala = es_generala(dados)

print(dados)
print(generala)
#%%
# Luego analizá el siguiente código. Correlo con `N = 100000` varias veces y observá los valores que obtenés. Luego correlo algunas veces con `N = 1000000` (ojo, hace un millón de experimentos, podría tardar un poco):
N = 1000000

G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

