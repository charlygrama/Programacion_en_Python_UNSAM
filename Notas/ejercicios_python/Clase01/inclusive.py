# Ejercicio 1.29: Traductor (rústico) al lenguaje inclusivo
# 'todes somes programadores'

frase = 'todos somos programadores'   
palabras = frase.split()
frase_t = ''
for palabra in palabras:
    if palabra[-2] == 'o':
        palabra[-2] = 'e' 
        print( frase_t )
