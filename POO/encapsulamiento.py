class Ejemplo:
	def __init__(self):
		self.__oculto = "Me encuentro oculto en la clase"

	def publico(self): #medodo publico
		return "Soy un metodo publico a la vista de todos!"

	def __privado(self): #metodo privado
		return "Soy un metodo privado para ti no existo"

	def get_oculto(self):
		return self.__oculto

	def set_oculto(self):
		self.__oculto = self.__privado()

#Instaciamos un objeto de la clase Ejemplo
objeto = Ejemplo()

#Accedemos al metodo publico

print(objeto.publico())

#Accedemos al metodo privado(no se puede)

#print(objeto.__privado())

#name mangling (para accesar a metodos privados)
print(objeto._Ejemplo__privado())

#llamamos a metodo oculto en clase

print(objeto.get_oculto())

print(objeto.set_oculto())