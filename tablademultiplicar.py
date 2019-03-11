tabla = range(1,11)
valor2 = int(input("Ingresa la tabla de multiplicar que deseas ver: "))
for valor in tabla:
	resultado = valor * valor2
	print(str(valor)+" x "+str(valor2)+" = "+str(resultado))
