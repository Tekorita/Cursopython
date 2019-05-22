#Un decorador nos va a permitir agregar mayor funcionalidad a una funcion en concreta
#por ejemplo A, B, C son funciones
#Un decorador es una funcion que recibe como parametro otra funcion para dar como salida una nueva funcion
#A recibe como parametro B para poder crear C
#EJEMPLO BASICO DE UN DECORADOR:
"""
def decorador(func): #A #B=func
	def nueva_funcion():
		print("Vamos a ejecutar la funcion")
		func() #B
		print("Se ejecuto la funcion")		
	return nueva_funcion #C

@decorador
def saluda():
	print("Hola Mundo")

saluda()

@decorador
def suma():
	print(10 + 20)

saluda()

"""
def decorador(is_valid):
	def _decorador(func): #A #B=func
		def before_action():
			print("Vamos a ejecutar la funcion primero")
		def after_action():
			print("Se ejecuto la funcion despues")

		def nueva_funcion(*args, **kwargs):
			if is_valid:
				before_action()

			resultado = func(*args, **kwargs)
			after_action()		
			return resultado
		return nueva_funcion #C
	return _decorador

"""
@decorador(is_valid = True)
def saluda():
	print("Hola Mundo")
"""

@decorador(is_valid = True)
def suma(num_uno, num_dos):
	return num_uno + num_dos

resultado = suma(90, 44)
print(resultado)

#ahora en el ultimo ejemplo podemos ver que los decoradores pueden pasar por una funcion
#en este caso encerraremos la funcion @decorador en otra que se llame @decorador donde le pasaremos
#como parametros un valor booleano

#donde si el booleano es falso no ejecuta la funcion before_action y si es True la ejecuta