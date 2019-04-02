palabra = "anita lava la tina"

def palindromo(palabra):
	palabra2 = palabra.replace(' ','')
	resultado = palabra2[::-1]
	if resultado == palabra2:
		print("La palabra es un palindromo gracias la gerencia")
	else:
		print("La palabra no es un palindromo gracias la gerencia")

palindromo(palabra)