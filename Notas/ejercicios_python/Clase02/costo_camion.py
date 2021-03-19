### Ejercicio 2.2: Lectura de un archivo de datos
with open('../Data/camion.csv', 'rt') as f:
    data = f.read()
print(data)

