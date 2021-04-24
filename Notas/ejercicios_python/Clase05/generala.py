# -*- coding: utf-8 -*-
### Ejercicio 5.2: Generala no necesariamente servida
# Si uno juega con las reglas originales (se puede volver a tirar algunos de los cinco dados hasta dos veces, llegando hasta a tres tiradas en total) siguiendo una estrategia que intente obtener generala (siempre guardar los dados que más se repiten y tirar nuevamente los demás) es más probable obtener una generala que si sólo consideramos la generala servida. Escribí un programa que estime la probabilidad de obtener una generala en las tres tiradas de una mano y guardalo en un archivo `generala.py`.
import random
from statistics import mode

# tiros = 1
def tirada():
    mano = []
    mano2 = []
    mano3 = []
    cant_rep = [] 
    generala = []
    cant_dados = 5
    manos = 2
    tamanio = 0
    
    while tamanio <= 5 and manos != 0:
        
        for i in range(cant_dados):
            mano.append(random.randint(1,6))
        manos -= 1
        moda = mode(mano)
        cant_rep = mano.count(moda)
        for i in range(cant_rep):
            generala.append(moda)
        cant_dados -= cant_rep
        tamanio = len(generala) 
        if tamanio >= 5:
            break
        
        for i in range (cant_dados):
            mano2.append(random.randint(1,6))
        manos -= 1
        if moda in mano2:
            cant_rep = mano2.count(moda)
            cant_dados -= cant_rep 
            for i in range(cant_rep):
                generala.append(moda)
            tamanio = len(generala) 
            if tamanio >= 5:
                break
       
        for i in range (cant_dados):
            mano3.append(random.randint(1,6))
        if moda in mano3:
            cant_rep = mano3.count(moda)
            cant_dados -= cant_rep       
            for i in range(cant_rep):
                generala.append(moda)
    
    return generala

def es_generala(generala):
    cond = False
    tamanio = len(generala)
    if tamanio == 5:
        for i in range(len(generala)):
            t = len(generala) - 1
            for j in range(t):
                if generala[i] == generala[j]:
                    cond = True
                else:
                    cond = False
                    break
    return cond
    
N = 1000000
G = sum([es_generala(tirada()) for i in range(N)])
prob = G/N
print(f'Jugué {N} veces, de las cuales {G} saqué generala no servida.')
print(f'la probabilidad de sacar generala no servida es= {prob:.2f}.')


