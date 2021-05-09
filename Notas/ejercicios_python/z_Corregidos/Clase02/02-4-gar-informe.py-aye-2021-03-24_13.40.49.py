#informe.py
import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote ={"nombre" : row[0],"cajones" : int(row[1]), "precio" : float(row[2])}
            camion.append(lote)
    return camion

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if row!=[]:
                precios[row[0]] = float(row[1])
    return precios

def balance(camion, precios):
    costo_camion = 0
    recaudacion = 0
    for s in camion:
        costo_camion += s['cajones']*s['precio']
        if s['nombre'] in precios:
            recaudacion += s['cajones']*precios[s['nombre']]
    diferencia = costo_camion - recaudacion
    return {"costo camión": costo_camion , "recaudación": recaudacion, "diferencia" : diferencia}

# python3 -i informe.py
precios = leer_precios('../Data/precios.csv')
camion = leer_camion('../Data/camion.csv')
balance = balance(camion, precios)
# balance
# {'costo camión': 47671.15, 'recaudación': 58964.1, 'diferencia': -11292.949999999997}
# hubo perdida :(
