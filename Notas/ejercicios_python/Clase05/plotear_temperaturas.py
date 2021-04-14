#%%
# -*- coding: utf-8 -*-
### Ejercicio 5.8: Empezando a plotear
# Escribí un archivo `plotear_temperaturas.py` que lea el archivo de datos  `Temperaturas.npy` con 999 mediciones simuladas que creaste recién y, usando el siguiente ejemplo, hacé un histograma de las temperaturas simuladas:
import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.loadtxt('../Data/Temperaturas.npy')
plt.hist(temperaturas,bins=200)



# Ajustá la cantidad de _bins_ para que el gráfico se vea lo mejor posible.

#%%

