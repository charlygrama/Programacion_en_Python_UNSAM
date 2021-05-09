#%%
# -*- coding: utf-8 -*-
### Ejercicio 5.5: Gaussiana

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

#%%
### Ejercicio 5.7: Guardar temperaturas

import random
import statistics as stats
import numpy as np

temperatura = []
N = 999
for i in range(N):
    temperatura.append(random.normalvariate(0, 0.2))
    print(f'{temperatura}', end=', ')
        
print('-'*40)
maximo = print('máximo: ', max(temperatura))
maximo = print('mínimo: ', min(temperatura))
promedio = print('promedio = ', sum(temperatura) / len(temperatura))
promedio = print('mediana = ', stats.median(temperatura))


array = np.array(temperatura)

np.savetxt('../Data/Temperaturas.npy', array)

np.loadtxt('../Data/Temperaturas.npy')

#%%