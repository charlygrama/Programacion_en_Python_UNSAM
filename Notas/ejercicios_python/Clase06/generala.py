# -*- coding: utf-8 -*-
### Ejercicio 5.2: Generala no necesariamente servida
# Si uno juega con las reglas originales (se puede volver a tirar algunos de los cinco dados hasta dos veces, llegando hasta a tres tiradas en total) siguiendo una estrategia que intente obtener generala (siempre guardar los dados que más se repiten y tirar nuevamente los demás) es más probable obtener una generala que si sólo consideramos la generala servida. Escribí un programa que estime la probabilidad de obtener una generala en las tres tiradas de una mano y guardalo en un archivo `generala.py`.
import random


def tirada():
    tirada = []
    dados = 5
    while dados > 0:
        tirada.append(random.randint(1,6))
        for p, d in enumerate(tirada):
            cant_rep = tirada.count(d)
            dados -= cant_rep
    return dados
            
         
    return cant_rep

generala = tirada() 
print(generala)

