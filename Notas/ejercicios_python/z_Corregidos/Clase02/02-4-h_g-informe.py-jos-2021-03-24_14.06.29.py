#informe.py

import csv

def leer_precios(nombre_archivo):
    f=open(nombre_archivo)
    filas = csv.reader(f)
       
    dic={}
    for fila in filas:
        try:
            dic[fila[0]]=float(fila[1])
        except:
            print('Fila vacia')
    return dic  
    
    
def leer_camion(nombre_archivo):
    f=open(nombre_archivo)
    filas = csv.reader(f)
    encabezados=next(filas)    
    camion = []
   
    for fila in filas:
        lote={encabezados[0]:fila[0],
              encabezados[1]:int(fila[1]),
              encabezados[2]:float(fila[2])}
        camion.append(lote)
    return camion
   
frutas=leer_precios('precios.csv')
camion=leer_camion('camion.csv')
total=0.0
venta=0.0
for s in camion:
    total += s['cajones']*s['precio']
    venta += frutas[s['nombre']]*s['cajones']

print(f'El costo del camion fue: {total}')
print(f'Lo que se recaudo con la venta fue: {venta}')
print(f'La diferencia fue: {venta-total}')



    









