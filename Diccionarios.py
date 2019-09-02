Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #los diccionarios permiten utilizar una clave para declarar y acceder a un valor y pueden ser inmutable
... 
>>> mi_diccionario = {'clave_1': 'valor1', 'clave_2': 2, 'clave_3': 5.67}
>>> print (mi_diccionario['clave_2'])
2
>>> print (mi_diccionario['clave_1'])
valor1
>>> print (mi_diccionario['clave_3'])
5.67
>>> 
>>> #podemos modificar una clave
... 
>>> mi_diccionario['clave_3'] = 'NUEVO VALOR 3'
>>> print (mi_diccionario)
{'clave_1': 'valor1', 'clave_2': 2, 'clave_3': 'NUEVO VALOR'}
>>> mi_diccionario = {'clave_1': 'valor1', 'clave_2': 2, 'clave_3': 5.67, (1, 6): [5, 6, 7]}
>>> print (mi_diccionario)
{'clave_1': 'valor1', 'clave_2': 2, 'clave_3': 5.67, (1, 6): [5, 6, 7]}
>>> print (mi_diccionario[(1, 6)])
[5, 6, 7]
>>> 