### Ejercicio 2.7: Buscar precios
def buscar_precio(nombre_fruta):
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as f:
        for linea in f:
            fila = linea.split(',')
            if fila[0] == nombre_fruta:
                precio = fila[1]
                print(precio)    

    return  
                
buscar_precio('Lima')
