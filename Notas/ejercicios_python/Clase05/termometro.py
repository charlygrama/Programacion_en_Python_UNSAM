# -*- coding: utf-8 -*-
# La distribución normal tiene muchos usos. Uno de ellos es modelar errores experimentales, es decir la diferencia entre el valor medido de una magnitud física y el valor real de dicha magnitud. 

# Hagamos algún ejercicio sencillo antes de terminar. Supongamos que una persona se compra un termómetro que mide la temperatura con un error aleatorio normal con media 0 y desvío estándar de 0.2 grados (error gaussiano). Si la temperatura real de la persona es de 37.5 grados, simulá usando `normalvariate()` (con `mu` y `sigma` adecuados) `n = 99` valores medidos por el termómetro.

# Imprimí los valores obtenidos en las mediciones de temperatura simuladas y luego, como resumen, cuatro líneas indicando el valor máximo, el mínimo, el promedio y la mediana de estas `n` mediciones. Guardá tu programa en el archivo `termometro.py`.
import random
import statistics as stats

temperatura = []
N = 99
for i in range(N):
    temperatura.append(random.normalvariate(0, 0.2))
    print(f'{temperatura}', end=', ')
        
print('-'*40)
maximo = print('máximo: ', max(temperatura))
maximo = print('mínimo: ', min(temperatura))
promedio = print('promedio = ', sum(temperatura) / len(temperatura))
promedio = print('mediana = ', stats.median(temperatura))
primer_quartil = print('primer quartil = ', temperatura)

