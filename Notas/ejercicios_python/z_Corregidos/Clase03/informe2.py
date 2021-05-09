# Ej. 2.15

#import csv
#
#def leer_camion(nombre_archivo):
#	'''lee el contenido del archivo y lo devuelve como una lista de tuplas'''
#	camion = []
#	with open(nombre_archivo, 'rt') as f:
#		rows = csv.reader(f)
#		headers = next(rows)
#		for row in rows:
#			lote = (row[0], int(row[1]), float(row[2]))
#			camion.append(lote)
#	return camion


# Ej. 2.16
# ahora me devuelve una lista de diccionarios 

#import csv
#from pprint import pprint
#
#def leer_camion(nombre_archivo):
#	'''lee el contenido del archivo y lo devuelve como una lista de diccionarios'''
#	camion = []
#	with open(nombre_archivo, 'rt') as f:
#		rows = csv.reader(f)
#		headers = next(rows)
#		i=0
#		for row in rows:
#			di = {}
#			di['nombre'] = row[0]
#			di['cajones'] = int(row[1])
#			di['precio'] = float(row[2])
#			i+=1
#			camion.append(di)
#	return camion
#
#pprint(leer_camion('../Data/camion.csv'))
#print(leer_camion('../Data/camion.csv'))


# Ej. 2.17
# creo un diccionario con los precios de casa item
# csv.reader es mejor que split porque saca solo los '/n' del final de casa linea
#import csv
# 
#def leer_precios(nombre_archivo):
#	f = open(nombre_archivo, 'rt')
#	d = {}
#	rows = csv.reader(f)
#	for row in rows:
#		if len(row) != 0:
#			d[row[0]] = float(row[1])
#	f.close()
#	return d

# para acceder al diccionario:
# algo = leer_precios(../Data....)
# algo['item']
# te tira el precio de item

# Ej. 2.18

#import csv
#from pprint import pprint
#
#def leer_camion(nombre_archivo):
#	'''lee el contenido del archivo y lo devuelve como una lista de diccionarios
#	cada diccionario tiene tres keys (nombre, precio, cajones)
#	y es un diccionario por item'''
#	camion = []
#	with open(nombre_archivo, 'rt') as f:
#		rows = csv.reader(f)
#		headers = next(rows)
#		i=0
#		for row in rows:
#			di = {}
#			di['nombre'] = row[0]
#			di['cajones'] = int(row[1])
#			di['precio'] = float(row[2])
#			i+=1
#			camion.append(di)
#	return camion
#
#
#def leer_precios(nombre_archivo):
#	''' Devuelve un diccionario con keys itmes y values precio'''
#	f = open(nombre_archivo, 'rt')
#	d = {}
#	rows = csv.reader(f)
#	for row in rows:
#		if len(row) != 0:
#			d[row[0]] = float(row[1])
#	f.close()
#	return d
#
#costo_camion = 0
#plata_venta = 0
#info_camion = leer_camion('../Data/camion.csv') #lista de dicc
#info_precio_venta = leer_precios('../Data/precios.csv') #dicc
#
#for dicc in info_camion:
#	costo_camion += dicc['cajones'] * dicc['precio']
#	plata_venta += dicc['cajones'] * info_precio_venta[dicc['nombre']]
#
#ganancia = plata_venta - costo_camion
#print('el costo del camion es ', costo_camion)
#print('la plata de la venta fue ', plata_venta)
#print('la ganancia es de ', round(ganancia,2))


# Ej. 3.9

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
	'''lee el contenido del archivo y lo devuelve como una lista de diccionarios
	cada diccionario tiene tres keys (nombre, precio, cajones)
	y es un diccionario por item'''
	camion = []
	with open(nombre_archivo, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for n_row,row in enumerate(rows, start=1):
			record = dict(zip(headers,row))
			try:
				camion.append(record)
			except ValueError:
				print(f'Fila {n_row}: No puede interpretar: {row}')
	return camion


def leer_precios(nombre_archivo):
	''' Devuelve un diccionario con keys itmes y values precio'''
	f = open(nombre_archivo, 'rt')
	d = {}
	rows = csv.reader(f)
	for row in rows:
		try:
			if len(row) != 0:
				d[row[0]] = float(row[1])
		except:
			pass
	f.close()
	return d

costo_camion = 0
plata_venta = 0
info_camion = leer_camion('G:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/fecha_camion.csv') #lista de dicc
info_precio_venta = leer_precios('G:/proyectos/python/python_UNSAM/Notas/ejercicios_python/Data/precios.csv') #dicc

for dicc in info_camion:
	costo_camion += int(dicc['cajones']) * float(dicc['precio'])
	plata_venta += int(dicc['cajones']) * float(info_precio_venta[dicc['nombre']])

ganancia = plata_venta - costo_camion
print('el costo del camion es ', costo_camion)
print('la plata de la venta fue ', plata_venta)
print('la ganancia es de ', round(ganancia,2))
