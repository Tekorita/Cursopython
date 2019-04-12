class perro:

    tipo = "canino"

    def __init__(self,nombre,raza,edad,dueño):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.dueño = dueño

    def ver_datos(self):
        print("Nombre: "+str(self.nombre))
        print("Raza: "+str(self.raza))
        print("Edad: "+str(self.edad))
        print("Dueño: "+str(self.dueño)) 

class Usuario:
    def __init__(self,usuario,password,email):
        self.usuario = usuario
        self.__password = self.__generar_password(password)
        self.email = email
        
    def __generar_password(self, password):
        return password.upper()

    def get_password(self):
        return self.__password

#caninos = perro("tina","mierdera",6,"David Palma")

#caninos.nombre = str(input("ingresa el nombre nuevo de tu perro o perra: "))
#caninos.raza = str(input("ingresa ahora la raza trata de que no sea mierdera: "))
#caninos.edad = int(input("ingresa los años del pobre perro: "))
#caninos.dueño = str(input("ingresa tu nombre ya que ahora seras su dueño: "))

#caninos.ver_datos()

user = str(input("Ingresa el usuario: "))
password = str(input("Ingresa la super clave bella: "))
email = str(input("Ingresa el email: "))

usuario1 = Usuario(user,password,email)

print(usuario1.email)
#print(usuario1.__password)







