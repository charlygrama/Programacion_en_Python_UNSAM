# Ejercicio 1.29: Traductor (rústico) al lenguaje inclusivo
# 'todes somes programadores'

frase = 'todos somos programadores'   
palabras = frase.split()
frase_t = ''
for palabra in palabras:
    palabra_nueva = list(palabra)
    if palabra[-2] == 'o':
        palabra_nueva[-2] = 'e' 
    frase_t += ''.join(palabra_nueva) + ' '
print(frase_t)
