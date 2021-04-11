# -*- coding: utf-8 -*-
### Ejercicio 5.2: Generala no necesariamente servida
# Si uno juega con las reglas originales (se puede volver a tirar algunos de los cinco dados hasta dos veces, llegando hasta a tres tiradas en total) siguiendo una estrategia que intente obtener generala (siempre guardar los dados que más se repiten y tirar nuevamente los demás) es más probable obtener una generala que si sólo consideramos la generala servida. Escribí un programa que estime la probabilidad de obtener una generala en las tres tiradas de una mano y guardalo en un archivo `generala.py`.
import random
from statistics import mode
tiradas = []
# tiros = 1
cant_rep = [] 
lista_repetidos = []
def tirada():
    cant_dados = 5
    while cant_dados > 0:
        for i in range(cant_dados):
            tiradas.append(random.randint(1,6))
        for p, e in enumerate(tiradas):
            rep = tiradas.count(e)
            cant_rep.append(rep)
            cant_veces = max(cant_rep)
        moda = mode(tiradas)
            
        print(f'tirada: {tiradas}')
        print(f'el número mas repetido es: {moda}')
        print(f'Se repite {cant_veces} veces')
        elegir = input('¿Elegir número? s/n : ')
        
        if elegir.lower() == 's':
            numero = input('número: ')
            for i in range(cant_veces):
                lista_repetidos.append(numero)
        else:
            pass
        cant_dados -= cant_dados
        
        for i in range(cant_dados):
            tiradas.append(random.randint(1,6))
        for p, e in enumerate(tiradas):
            rep = tiradas.count(e)
            cant_rep.append(rep)
            cant_veces = max(cant_rep)
        moda = mode(tiradas)
        for i in tiradas:
            if not numero in tiradas:
                cant_dados = cant_dados
            else:
                lista_repetidos.append(numero)
                cant_dados -= cant_dados
    return cant_veces, moda

generala = tirada() 
print(generala)

