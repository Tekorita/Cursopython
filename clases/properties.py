#Con las property vamos a poder tener acceso y modificar los metodos o variables privadas q empiezen con __

#todo metodo o atributo que empieze por doble guion bajo __ es una instancia a atributos privados

class Usuario:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password)
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	#def get_password(self):
	#	return self.__password

	@property
	def password(self):
		return self.__password

	@password.setter #para modificar una variable privada
	def password(self, valor):
		self.__password = self.__generar_password(valor)

David = Usuario('David','david123','davidpalmalugo@gmail.com')
#print(David.username)
#print(David.get_password())
#print(David.email)
print(David.password)
David.password = "nueva clave"
print(David.password)	