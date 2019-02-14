Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #Las condicionales nos permiten evaluar si una o mas se cumplen para poder tomar una decision
... 
>>> if (1==1)
  File "<stdin>", line 1
    if (1==1)
            ^
SyntaxError: invalid syntax
>>> numero = 1
>>> if numero > 0:
... 	print("numero es positivo")
... 
numero es positivo
>>> numero = -6
>>> if numero > 0:
... 	print("numero es positivo")
... else:
... 	print("numero es negativo")
... 
numero es negativo
>>> numero = 0
>>> if numero > 0:
... 	print("numero es positivo")
... elif numero < 0:
... 	print("numero es negativo")
... else:
... 	print("numero es igual a 0")
... 
numero es igual a 0
>>> 