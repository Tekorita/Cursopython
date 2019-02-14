class Circulo:

	#los metodos estaticos son aquellas funciones dentro de una clase que no contienen la palabra reservada self
	#y para que sean estaticos se tienen que decorar
	#los metodos estaticos son metodos que le pertenecen directamente a la clase y no a la instancia 
	
	@staticmethod
	def pi():
		return 3.1416

	def __init__(self, radio):
		self.radio = radio

	def area(self): #metodos de instancia si tiene la palabra self y esta dentro de la clase
		return self.radio * self.radio * Circulo.pi()



circulo_uno = Circulo(4)

print(circulo_uno.area())
print(Circulo.pi())