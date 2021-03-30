## Ejercicio 3.17: Tablas de multiplicar
l = []
t = 0
for i in range(0,10):
    for j in range(0,10):
        print('{:3}'.format(i * j), end=' ')
        l.append(i)

    # t += 1
# print(f'{l}')

# for i in l:
#     print(l[i]) 
#     i += 1
# print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}')
# :>10d   Entero alineado a la derecha en un campo de 10 caracteres
    
