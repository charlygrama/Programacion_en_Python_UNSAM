# Ej. 4.9
# En este ejercicio me ayudó Manuela Saenz que me dio la idea de hacer el for para atrás y para adelante

import copy

def propagar(vector):
	'''reciba un vector con 0's, 1's y -1's y devuelva un 
	vector en el que los 1's se propagaron a sus vecinos con 0
	'''
	vector_prop = copy.deepcopy(vector)
	longitud = len(vector_prop)
# recorro la lista hacia adelante
	i = 0 # inicializo el índice en el primer elemento
	while i < (longitud - 1): #llega hasta el anteúltimo elemento
		if (vector_prop[i] == 1 and vector_prop[i+1] == 0): 
			vector_prop[i+1] = 1 # propago en el caso de encontrar un 1 seguido de un 0
		i += 1 # avanzo en el vector

# recorro la lista hacia atrás
	j = longitud - 1 # inicializo el índice en el último elemento (ya que un vector de long 8 tiene el ultimo undice de 7)
	while j > 0: # llega hasta el segundo elemento
		if (vector_prop[j] == 1 and vector_prop[j-1] == 0): 
			vector_prop[j-1] = 1 # propago en el caso de encontrar un 0 seguido de un 1
		j -= 1 # retrocedo en el vector

	return vector_prop


print(propagar([ 0, 0, 0, 1, 0, 0]))
print(propagar([0,0,0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
print(propagar([1,0,-1,0,1,-1]))
print(propagar([1,1,0,0,-1,0,-1,-1,1,0]))

# Salida:
# [1, 1, 1, 1, 1, 1]
# [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
# [1, 1, -1, 1, 1, -1]
# [1, 1, 1, 1, -1, 0, -1, -1, 1, 1]




#def propagar(vector):
#	'''reciba un vector con 0's, 1's y -1's y devuelva un 
#	vector en el que los 1's se propagaron a sus vecinos con 0
#	'''
#	#vector_1 = [1,1,1,1,1,1]
#	vector_1 = [1,1,1,1,1,1,1,1,1,1,1,1,1]
#	while vector != vector_1:
#		for i,n in enumerate(vector):
##				print(vector)
#			if i != (len(vector)-1) and i != 0:
#				if n == 1 and (vector[i+1] != -1 or vector[i-1] != -1):
#					print('hola')
#					if vector[i-1] == 0:
#						vector[i-1] = 1
#					if vector[i+1] == 0:
#						vector[i+1] = 1
#					if (vector[i+1] == -1 or vector[i+1] == 1) and (vector[i-1] == -1 or vector[i-1] == 1) :
#						print('aca')
#						return (vector)
#					#	print(vector)
#	#		else:
#	#			pass
#	return(vector)
