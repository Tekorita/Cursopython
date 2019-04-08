#una frase palindromo es una serie de caracteres o numeros que se lee igual de derecha a izquierda y viceversa

def palindromo (frase):
	frase = frase.replace(' ','') #variables locales
	return frase == frase[::-1]

frase = 'anita lava la tina' #variables Globales
resultado = palindromo(frase)
print(resultado) 

#Las variables globales no pueden ser modificadas dentro de una funcion ejemplo

def valor_global():
	variable_global = 'Cambiar valor' #variable locales

variable_global = 'esto es una variable global entiende!!'

print(variable_global)
valor_global()
print(variable_global)

#ahora hacemos un ejemplo de como cambiando una variable local a global podemos modificar otra variable global

def valor_global2():
	global variable_global2 
	variable_global2 = 'Cambiar valor' #variable locales

def mostrar_global():
	print(variable_global2)

def crear_global():
	global nueva_variable
	nueva_variable = 'drojannnnsi drojansi'

variable_global2 = 'esto es una variable global'

print(variable_global2)
valor_global2()
print(variable_global2)

crear_global()
print(nueva_variable)
