class Lapiz: #Plantilla clase
	#color = "Amarillo" #Atributos
	#contiene_borrador = False
	#usa_grafito = True
	#Metodos

	def __init__(self, color = "Amarillo", contiene_borrador = False, usa_grafito = False):
		self.color = color #Atributos
		self.contiene_borrador = contiene_borrador
		self.usa_grafito = usa_grafito

	def dibujar(self):
		print("El Lapiz esta dibujando.")

	def borrar(self):
		if self.es_valido_para_borrar():
			print("El Lapiz esta borrando.")
		else:
			print("No es posible Borrar")

	def es_valido_para_borrar(self):
		return self.contiene_borrador #self. para llamar un atributo dentro de un metodo





#Esto es un objeto instanciado
lapiz_generico = Lapiz("verde", True, True)
lapiz_generico.dibujar()
#lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()