Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def mi_funcion():
... 	"""Primera funcion en python"""
... 	print("Hola a todos")
... 	print("esta es mi primera funcion en python")
... 
>>> mi_funcion()
Hola a todos
esta es mi primera funcion en python
>>> mi_funcion()
Hola a todos
esta es mi primera funcion en python
>>> mi_funcion()
Hola a todos
esta es mi primera funcion en python
>>> def mi_funcion2(cadena, numero):
... 	"""Escribe una cadena de texto el numero de veces que le asignemos al numero"""
... 	print(cadena * numero)
... 
>>> mi_funcion2("Tina", 8)
TinaTinaTinaTinaTinaTinaTinaTina
>>> def mi_funcion3(cadena, numero = 4):
... 	"""Escribe una cadena de texto por default 4 veces"""
... 
>>> mi_funcion3("Tekorita ")
>>> 
>>> mi_funcion3("Tekorita ",5)
>>> 
>>> mi_funcion3("Tekorita ",5)
>>> def mi_funcion3(cadena, numero = 4):
... 	"""Escribe una cadena de texto por default 4 veces"
... """
... 
>>> 	print(cadena*numero)
  File "<stdin>", line 1
    print(cadena*numero)
    ^
IndentationError: unexpected indent
>>> def mi_funcion3(cadena, numero = 4):
... 	"""Escribe una cadena de texto por default 4 veces"""
... 	print(cadena*numero)
... 
>>> mi_funcion3("Tekorita ",5)
Tekorita Tekorita Tekorita Tekorita Tekorita 
>>> mi_funcion3("Tekorita ")
Tekorita Tekorita Tekorita Tekorita 
>>> def cuadrado1(num):
... 	"""Muestra el cuadrado de un numero"""
... 	print(num * num)
... 
>>> cuadrado1(9)
81
>>> def cuadrado2():
... 	"""Imprime el cuadrado de numero ingresado"""
... 	n = int(input("Ingrese un numero: "))
... 	cuadrado1(n)
... 
>>> cuadrado2()
Ingrese un numero: 8
64
>>> print(cuadrado2())
Ingrese un numero: 7
49
None
>>> def cuadrado3_return():
... 	"""Retorna el cuadrado de un numero"""
... 	n = int(input("Ingrese un numero: "))
... 	return n * n
... 
>>> cuad = cuadrado3_return()
Ingrese un numero: 8
>>> cuad = cuadrado3_return()
Ingrese un numero: 9
>>> print(cuad)
81
>>> 