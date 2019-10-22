#La documentacion o el docstring de una funcion va justo despues en la primera linea dentro de la funcion

def generador(*args):
	"""Recibe n cantidad de numero y regresa el numero ademas de regresa \nTrue o False si el numero es mayor a 5
	"""
	for valor in args:
		yield valor * 10, True if valor > 8 else False #Un ejemplo

nombre = generador.__name__ #para ver el nombre de la funcion
documentacion = generador.__doc__ #para ver la documentacion de la funcion
print(nombre, " : ")
print(documentacion)

#Para ver la documentacion desde el interprete de python por consola entramos al prompt de python
#Luego invocamos de esta manera
#from 'nombre de archivo' import 'funcion'
#luego escribimos help('funcion') 

