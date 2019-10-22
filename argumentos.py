#los argumentos son parametros indefinidos que uno puede pasar por parametros en una funcion con la instancia de * convirtiendose en tuplas
#y usando ** se convierten en diccionarios

def suma(*argumento):
	print(argumento)

resultado = suma(10,50,20,45)
print(resultado)

#luego todo lo que se puede hacer con tuplas se puede aplicar

#en python por defecto se escribe *args y no argumentos 

def suma1(*args):
	resultado = 0
	for valor in args:
		resultado = resultado + valor
	return resultado

resultado = suma1(1,2,3,4,5,6,7,8,9,10,11,12,13)
print(resultado)

#tambien podemos trabajar con diccionarios y mostrar el nombre de las variables tambien

#en python por defecto se escribe **kwargs y no argumentos

def suma2(**kwargs):
	print(kwargs)

resultado = suma2(nombre = 'David', edad = 28, estatura = 1.80, hombre = True)
print(resultado)

