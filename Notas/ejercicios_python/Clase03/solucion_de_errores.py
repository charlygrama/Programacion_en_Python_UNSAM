#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era que la función no recorria la expresion y returnaba el valor muy pronto.
#    Lo corregí :
            # * haciendo que la funcion recorra la epresion y retorne True si encuentra una 'a'.
            # * gardando en una variable cuando el valor de False para q continue recorriendo la expresion.
            # * cuando termina de recorrer la expresion retorna el valor.
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            a = False
        i += 1
    return a
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.