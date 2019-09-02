tabla = range(1,11)
valor2 = int(input("Ingresa la tabla de multiplicar que deseas ver: "))
for valor in tabla:
	resultado = valor * valor2
	print(str(valor)+" x "+str(valor2)+" = "+str(resultado))

def tablaDeMultiplicar(valor):
    for num in range(1,11):
        resultado = valor * num
        print(str(valor)+" x "+str(num)+" = "+str(resultado))

valor1 = int(input("Ingresa el numero de la tabla de multiplicar para hacer el calculo :)"))
tablaDeMultiplicar(valor1)
