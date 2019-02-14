#Programacion orientada a objetos POO

class MiClaseEjemplo:
	""" Esto es un ejemplo de clases, objetos y metodos"""
	entero = 4321
	def mensaje(self, msj):
		print(msj)

	#instanciamos de la clase y asignamos el objeto a las variables
x = MiClaseEjemplo()
y = MiClaseEjemplo()

print(x.entero)
print(y.mensaje("HOla POO"))

