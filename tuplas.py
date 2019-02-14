Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #variable que permite almacenar varios y diversos tipos de datos inmutables que no se pueden modificar
... 
>>> mi_tupla = ('indice cero', 3, 3.70, 'indice tres')
>>> print (mi_tupla[0])
indice cero
>>> print (mi_tupla[1])
3
>>> print (mi_tupla[2])
3.7
>>> print (mi_tupla[3])
indice tres
>>> print (mi_tupla[-1])
indice tres
>>> print (mi_tupla[-2])
3.7
>>> print (mi_tupla[-3])
3
>>> print (mi_tupla[-4])
indice cero
>>> #se puede hacer slicing o rebanadada para buscar datos
... 
>>> print (mi_tupla[1:3]) 
(3, 3.7)
>>> print (mi_tupla[:3])
('indice cero', 3, 3.7)
>>> print (mi_tupla[1:])
(3, 3.7, 'indice tres')
>>> 
>>> 