class Circulo:

	pi = 3.1416 #las variables de clases son las que le pertenecen a la clase y no al objeto

	def __init__(self, radio):
		self.radio = radio

	def area(self):
		return self.radio * self.radio * self.pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

print(Circulo.pi) #no necesito crear un objeto para usar pi

print(circulo_uno.pi)
print(circulo_dos.pi)
print(circulo_uno.area())

#para saber si una variable de clase es o no es se consulta con la opcion de __dict__
#de no salir la variable quiere decir q es una varibale de clase

print(circulo_uno.__dict__)