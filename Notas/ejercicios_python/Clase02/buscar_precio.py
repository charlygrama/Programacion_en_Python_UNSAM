### Ejercicio 2.7: Buscar precios
def buscar_precio(nombre_fruta):
    encontrado = False
    with open('g:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/precios.csv', 'rt') as f:
        for linea in f:
            fila = linea.split(',')
            if fila[0] == nombre_fruta.capitalize():
                encontrado = True
                precio = fila[1]
                print('El precio de la',nombre_fruta,'es de: ', precio)

        if encontrado == False:
            print ('la fruta',nombre_fruta, 'no figura en el listado')          

buscar_precio('Papa')
