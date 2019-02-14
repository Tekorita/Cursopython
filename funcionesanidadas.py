# primero realizamos 2 ejemplos para poder entender las funciones anidadas
#donde visualizamos que dentro de una funcion invocamos a otra para realizar una validacion
"""
def validacion(num_uno, num_dos):
	return num_uno > 0 and num_dos > 0

def division(num_uno, num_dos):
	if validacion(num_uno, num_dos):
		return num_uno / num_dos

resultado = division (10,2)
print(resultado)
"""
#Ahora desarrollaremos funciones anidadas y es que consiste en crear una funcion dentro de otra

def division(num_uno, num_dos):
	def validacion(): #esta es una funcio anidada
		return num_uno > 0 and num_dos > 0

	if validacion():
		return num_uno / num_dos

resultado = division (10,2)
print(resultado)

#En las funciones anidadas existen los closures que es crear una funcion dentro de otra funcion sin ser llamada
#El termino de closures es que son funciones que crean a otras funciones y se retorna la nueva funcion creada


def crear_funcion(num_uno, num_dos): #closure
	def validacion():
		return num_uno > 0 and num_dos > 0
	return validacion #retornamos una funcion anidada

nueva_funcion = crear_funcion(10, 5)
print(nueva_funcion())

#en conclusion los closures son funciones que crean otra funciones

#ahora hacemos un ejemplo donde una funcion recibe como parametro otra funcion

def aplicar_funcion(func):
	resultado = func()
	print(resultado)

nueva_funcion = crear_funcion(10, 9)
aplicar_funcion(nueva_funcion)

