Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> class Aeronave:
... 	def viajar(self):
... 		print("Yo viajo por los aires")
... 
>>> class Automovil:
... 	def viajar(self):
... 		print("Yo viajo por los caminos")
... 
>>> zeppelin = Aeronave()
>>> Coche = Automovil()
>>> 
>>> zeppelin.viajar() #Se imprime de manera automatica sin necesidad de usar print
Yo viajo por los aires
>>> Coche.viajar() #Se imprime de manera automatica sin necesidad de usar el print
Yo viajo por los caminos
>>> 