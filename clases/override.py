#SOBRESCRIBIR UN METODO ES TOMAR EL METODO DE UNA CLASE PADRE Y CAMBIARLE LA FUNCIONALIDAD O AGREGARLE MAYOR FUNCIONALIDAD

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

class Mascota:

	def __init__(self, nombre): #Sobrescritura de instancias ahora tendria que pasar el nombre por parametros en linea 32
		self.nombre = nombre

	def mostrar_nombre(self):
		print(self.nombre)

class Gato(Felino, Mascota):
	def __ini__(self, nombre):
		Mascota.__init__(self, nombre)
		self.nombre_gato = nombre

	def gato_cazador(self):
		self.cazar()

	def mostrar_nombre(self): #Sobrescritura de metodos
		Mascota.mostrar_nombre(self)
		print("EL Nombre o apodo del gato es: {}".format(self.nombre))



gato = Gato("Patricio")

#gato.nombre = 'Patricio'
gato.mostrar_nombre()