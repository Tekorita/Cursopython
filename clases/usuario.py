#todo metodo o atributo que empieze por doble guion bajo __ es una instancia a atributos privados

class Usuario:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password)
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	def get_password(self):
		return self.__password

David = Usuario('David','david123','davidpalmalugo@gmail.com')
print(David.username)
print(David.get_password())
print(David.email)	