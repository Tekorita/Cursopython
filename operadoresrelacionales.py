Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #Operadores relacionales
... 
>>> print(10 == 12) #Resultado: falso
False
>>> print(10 == 10) #Resultado: verdadero
True
>>> 
>>> print(10 != 10) #Resultado: falso
False
>>> print('azul' != 'AZUL') #Resultado: verdadero
True
>>> print(8 < 9) #Resultado: verdadero
True
>>> print(9 < 9) #Resultado: False
False
>>> print(1 <= 1) #Resultado: verdadero
True
>>> print(1 <= 0) #Resultado: verdadero
False
>>> lista_uno = [1,2,3]
>>> lista_dos = [1,2,4]
>>> print(lista_uno == lista_dos)
False
>>> lista_dos = [1,2,3]
>>> print(lista_uno == lista_dos)
True
>>> tupla_uno = (1,2,'hola')
>>> tupla_dos = (1,2,'hola')
>>> print(tupla_uno == tupla_dos)
True
>>> 