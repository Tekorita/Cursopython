class Animal: #Clase Padre 1
	@property
	def terrestre(self):
		return True

class Felino(Animal): #Clase Padre 2
	@property
	def garras_retractiles(self):
		return True

	def cazar(self):
		print("El Felino esta casando")

#para que un metodo herencia propiedades de la misma clase se pasa por parametros el nombre de la clase
			
class Gato(Felino):
	def gato_cazador(self):
		self.cazar()

class Jaguar(Felino):
	pass

gato = Gato()
jaguar = Jaguar()

print(gato.cazar())
print(jaguar.garras_retractiles)
print(gato.terrestre)
