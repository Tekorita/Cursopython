#Los generadores nos sirven para crear objetos sin necesidad de guardalos en la memoria ram como suceden con enumerate o range o un for
#En este ejemplo vamos a crear nuestro propio generador
#la palabra clave para un generador es yield

def generador(*args):
	for valor in args:
		yield valor * 30, True #Un ejemplo

for valor_uno, valor_dos in generador(1,2,3,4,5,6,7,8,9):
	print(valor_uno, valor_dos)

for input1, input2 in generador(1,2,3,4):
	print(valor_uno, valor_dos)

for input3, input4 in generador(1,2,3):
	print(valor_uno, valor_dos) 

for input1, input2 in generador(1,2,3,4):
	print(valor_uno, valor_dos)

for input3, input4 in generador(1,2,3):
	print(valor_uno, valor_dos) 