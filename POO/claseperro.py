class MiPerro:
	"""Segundo ejemplo para el manejo y comprension de clases,
		objetos y metodos. con metodo __init__"""
	def __init__(self, raza): #MEtdoo que se ejecuta al instanciar
		#print("Todos somos objetos")
		self.raza = raza

	def ladrar(self, ladrido):
		print(ladrido)

	def juego(self, jugar):
		print(jugar)

	def proteger(self, cuidar):
		print(cuidar)

# Instanciamos dos objetos de la clase MiPerro

getrudis = MiPerro("Dalmata")
parker = MiPerro("Pastor")

#Accedemos a su atributo
print(getrudis.raza)
print(parker.raza)

# Accedemos a los metodos

getrudis.ladrar("Guau Guau me llamo tina y soy una: ")
parker.ladrar("Guau Guau me llamo parker Hola! y soy un: ")

