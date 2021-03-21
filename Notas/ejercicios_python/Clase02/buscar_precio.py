### Ejercicio 2.7: Buscar precios
def buscar_precio(nombre_fruta):
    encontrado = False
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as f:
        for linea in f:
            fila = linea.split(',')
            if fila[0] == nombre_fruta:
                encontrado = True
                precio = fila[1]
                print(precio)
            

        if encontrado == False:
            print('la fruta no figura en el listado')          
                
buscar_precio('Papa')
