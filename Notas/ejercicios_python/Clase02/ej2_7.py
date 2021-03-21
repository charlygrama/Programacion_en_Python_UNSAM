### Ejercicio 2.7: Buscar precios
costo_total = 0
with open('../Data/precios.csv', 'rt') as f:
    headers = next(f).split()
    for linea in f:
        fila = linea.split(',')
        if fila[0] == 'Naranja':
            precio = fila[1]
    
    print(precio)