def suma(valor_uno, valor_dos, valor_tres):
	return valor_uno + valor_dos + valor_tres

def division(valor_uno, valor_dos):
	return valor_uno / valor_dos

def multiplicacion(valor_uno, valor_dos = 10):
	return valor_uno * valor_dos

def multiples_valores():
	return 'String', 1, True, 56.9	

resultado1 = suma(10, 20, 30)
print(resultado1)

resultado2 = division(100,10)
resultado3 = division(valor_dos = 10, valor_uno = 100)
resultado4 = multiplicacion(3, 5)

resultado5 = multiples_valores()

#ahora vamos a imprimir multiples valores desglosando la tupla

string = resultado5[0]
entero = resultado5[1]
bol = resultado5[2]
floa = resultado5[3] 

print(string)
print(entero)
print(bol)
print(floa)

#lo optimizamos

string, entero, bol, floa = multiples_valores()

#podemos asignarle a una variable una funcion

mi_variable = multiplicacion

resultado6 = mi_variable(6, 7)
print(resultado6)

#podemos pasar por parametros de una funcion otra funcion o ejecutar dentro de una funcion otra funcion

def mostrar_resultado(funcion):
	print(funcion(5,5))

mi_variable2 = multiplicacion

mostrar_resultado(mi_variable)

