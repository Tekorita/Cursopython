class CasaStark: #Super clase/ clase base
	"""Personajes de game of thrones
	   Casa Stark"""
	print("Hijos de Eddard Stark y Lady Catelyn")
	def __init__(self, apellido_stark):
		self.apellido_stark = apellido_stark

class CasaTargaryen: #Super clase/ clase base
	"""Personajes de game of thrones
	   Casa Targaryen"""
	print("Hijos de Aerys - El rey loco")
	def __init__(self, apellido_targaryen):
		self.apellido_targaryen = apellido_targaryen

class HerederoStark(CasaStark): #Sub clase /clase hija o derivada
	"""Sub/clase que hereda de la clase CasaStark"""
	def nombre(self, nombre, apellido_stark):
		print("Mi nombre es ", nombre, " Heredero de la casa ", apellido_stark)

class HerederoTargaryen(CasaTargaryen): #Sub clase /clase hija o derivada
	"""Sub/clase que hereda de la clase CasaTargaryen"""
	def nombre_t(self, nombre_t, apellido_targaryen):
		print("Mi nombre es ", nombre_t, " Heredero de la casa ", apellido_targaryen)

#INstaciamos objetos de la clase derivada HerederoStark

robb = HerederoStark("Stark")
sansa = HerederoStark("Stark")
arya = HerederoStark("Stark")
bran = HerederoStark("Stark")
rickon = HerederoStark("Stark")

#INstaciamos objetos de la clase derivada HerederoTargaryen
daenerys = HerederoTargaryen("Targaryen")
vicerys = HerederoTargaryen("Targaryen")


#Accedemos a metodos y atributos (objeto.metodo)

print(robb.nombre("Robb ", robb.apellido_stark))
print(sansa.nombre("Sansa ", sansa.apellido_stark))
print(arya.nombre("Arya ", arya.apellido_stark))
print(bran.nombre("Bran ", bran.apellido_stark))
print(rickon.nombre("Rickon ", rickon.apellido_stark))

#Accedemos a metodos y atributos (objeto.metodo)

print(daenerys.nombre_t("Daenerys ", daenerys.apellido_targaryen))
print(vicerys.nombre_t("Vicerys ", vicerys.apellido_targaryen))
