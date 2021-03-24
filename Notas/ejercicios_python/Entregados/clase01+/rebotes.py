# rebotes.py
# Ejercicio 1.5: La pelota que rebota
salto = 0
altura = 100
h = 3/5
while salto <= 9:
    salto += 1
    altura *= h
    print(salto, round( altura , 4 ))
