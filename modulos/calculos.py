#!/usr/bin/python

"""
En este modulo se encarga de procesar las funciones de una calculadora
"""

__author__ = "David Jesus Palma Lugo"
__copyright__ = "Todos los derechos reservados 2018"
__credits__ = "CodeTekorita"

__license__ = "GLP"
__version__ = "1.0.1"
__maintainer__ = "David Palma"
__email__ = "davidpalmalugo@gmail.com"
__status__ = "desarrollador"

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
	
#para probar o consultar la documentacion y metadata del modulo entramos al prompt de python y escribimos:
#import calculos
#luego help(calculos)
#tambien podemos colocar dir(calculos) y nos regresas todos los atributos del modulo en lista


