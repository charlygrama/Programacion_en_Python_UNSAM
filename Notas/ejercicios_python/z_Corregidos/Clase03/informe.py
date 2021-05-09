#Titulo: informe.py (Ejercicio 3.19)
#Alumno: Alejandro Bossert - Email: alejandrobossert@gmail.com
#Descripción: Realiza una lectura del archivo Precios.csv y lo almacena en un 
#diccionario para facilitar la busqueda del precio de venta
#Realiza una lectura del archivo camion.csv y los almacena en una lista 
#para recorrerlo facilmente.
#Finalmente entrega la salida con la descripcion de la fruta, total importe
#de compra, total importe de venta, y la diferencia de ambos totales


import csv

def leer_precios(nombre_archivo): 
    f=open(nombre_archivo, encoding='utf-8')
    rows=csv.reader(f)
    record={}
    for row in rows:
        if row!=[]:
            record[row[0]]=row[1]
    return record




def costo_camion(nombre_archivo):
    Precios=leer_precios('G:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/precios.csv')
    L_camion=[]
    f=open(nombre_archivo, encoding='utf-8')
    rows= csv.reader(f)
    header=next(rows)
    costo_total=0
    ganancia_total=0
    for n_row,row in enumerate(rows,start=1):
        record=dict(zip(header,row))
        try:
            ncajones=int(record['cajones'])
            precio=float(record['precio'])
            costo_total+=ncajones*precio
            fruta=record['nombre']
            ganancia_total+=ncajones*float(Precios[fruta])  
            
        except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')  
                
    print (f'costo total:{costo_total} ganancia total:{ganancia_total} ganancia neta:{round(ganancia_total-costo_total,2)}')

costo_camion('G:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/fecha_camion.csv')
