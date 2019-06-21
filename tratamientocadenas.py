#Tratamiento de cadenas en python

cadena = input("Digite una cadena de texto o string o letras puess: ")

#Obtiene longitud de la cadena

print ("\nEl numero de caracteres de la cadena es: ", len(cadena))

#Devuelve True si la cadena contiene solo letras
if cadena.isalpha():
	print("\nLa cadena es alfabetica o de letras puess")

#Devuelve true si la cadena contiene solo numeros

if cadena.isdigit():
	print("\nLa cadena es numerica")

#COnvierte la cadena a mayusculas
print("\nEn Mayuscululas: ", cadena.upper())

#Convierte la cadena a minusculas
print("\nEn Minisculas: ", cadena.lower())

#COnvierte mayusculas a minisculas y viceversa

print("\nInvierte mayusculas y minisculas: ", cadena.swapcase())

#Remplazar
print("Reemplaza a por x", cadena.replace("a","x"))

#Devuelve la posicion del caracter solicitado (la primer insidencia)
print("\nLa posicion del caracter solicitado es: ", cadena.find("a"))

#Devuelve la posicion del carcter solicitado (la ultima insidencia)
print("\nLa posicion del carter solicitado es: ", cadena.rfind("a"))

#crea una lista de sub-cadenas de la cadena
print("Lista de sub-cadenas: ", cadena.split("a"))