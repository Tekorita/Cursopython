try:
	#print(2/0)
	lista = [1,2]
	print(lista[9])
except IndexError as ex:
	print(ex)
	print("No es posible obtener el valor en la lista o tupla")
except ZeroDivisionError as ex:
	print(ex)
	print("no se puede dividir por cero")
except Exception as ex:
	print(ex)
	print("no se que paso pero paso algo malo")
finally:
	print("Se termino el script de igual manera")
print("Se termino el script")

