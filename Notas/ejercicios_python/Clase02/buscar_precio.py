### Ejercicio 2.7: Buscar precios
# costo_total = 0
def buscar_precio(nombre_fruta):
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as f:
        headers = next(f).split()
        for linea in f:
            fila = linea.split(',')
            if fila[0] == nombre_fruta:
                precio = fila[1]

                
        print(precio)
                

buscar_precio('Lima')
