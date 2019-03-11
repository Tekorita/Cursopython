Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> respuesta = "si"
>>> numero = 0
>>> while respuesta == "si"
  File "<stdin>", line 1
    while respuesta == "si"
                          ^
SyntaxError: invalid syntax
>>> while respuesta == "si":
... 	numero = int(input("digite un numero: "))
... 	if numero > 0:
... 		print("El numero ingresado es positivo")
... 	elif numero < 0:
... 		print("El numero ingresado es negativo")
... 	else:
... 		print("El numero ingresado es igual a cero")
... 
digite un numero: 0
El numero ingresado es igual a cero
digite un numero: -3
El numero ingresado es negativo
digite un numero: 6
El numero ingresado es positivo
digite un numero: 6
El numero ingresado es positivo
digite un numero: =
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: invalid literal for int() with base 10: '='
>>> while respuesta == "si":
...   numero = int(input("digite un numero: "))
... 	if numero > 0:
... 		print("El numero ingresado es positivo")
... 	elif numero < 0:
... 		print("El numero ingresado es negativo")
... 	else:
... 		print("El numero ingresado es igual a cero")
... 	respuesta = input("Quieres ingresar otro numero? <si - no>")
... 
digite un numero: 9
El numero ingresado es positivo
Quieres ingresar otro numero? <si - no>no
>>> 

