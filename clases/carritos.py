class japoneses:

	def __init__(self, marca, modelo, ano, transmision, status = False):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.transmision = transmision
		self.status = status

	def verdatos(self):
		print("Marca: "+self.marca)
		print("Modelo: "+self.modelo)
		print("ano: "+self.ano)
		print("transmision: "+self.transmision)

	def status_venta(self):
		return self.status

	def verificar_status(self):
		if self.status_venta():
			print("Status: Disponible")
		else:
			print("Status: Vendido")


jdm = japoneses("mitsubishi", "eclipse","99","sincronico",True)

jdm.verdatos()
jdm.verificar_status()
