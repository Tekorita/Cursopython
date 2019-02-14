def suma():
	"""MUestra la suma de dos numeros ingresados"""
	a = int(input("Ingrese un numero entero: "))
	b = int(input("Ingrese un numero entero: "))
	print(a + b)

def resta():
	"""MUestra la resta de dos numeros ingresados"""
	a = int(input("Ingrese un numero entero: "))
	b = int(input("Ingrese un numero entero: "))
	print(a - b)

def multiplicacion():
	"""MUestra la multiplicacion de dos numeros ingresados"""
	a = int(input("Ingrese un numero entero: "))
	b = int(input("Ingrese un numero entero: "))
	print(a * b)

def dividir():
	"""MUestra la division de dos numeros ingresados"""
	a = int(input("Ingrese un numero entero: "))
	b = int(input("Ingrese un numero entero: "))
	print(a / b)

def fib(n):
	"""Muestra la serie fibonacci hasta el numero n"""
	x, y = 0, 1
	while x < n:
		print(x)
		x, y = y, x+y 
	print() #salto de linea
	



