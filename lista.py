poiPython 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #las listas a diferencia de las tuplas permiten modificar almacenados
... 
>>> mi_lista = ['indice cero', 4, 8.96, True, ['segunda lista', 90]]
>>> print (mi_lista[3])
True
>>> print (mi_lista[4])
['segunda lista', 90]
>>> print (mi_lista[-2])
True
>>> print (mi_lista[1:3])
[4, 8.96]
>>> #se puede modificar los valores tambien ejemplo:
... 
>>> mi_lista[0] = 'indice uno'
>>> print (mi_lista[0])
indice uno
>>> mi_lista[1:4] = [7, 9, 10]
>>> print (mi_lista)
['indice uno', 7, 9, 10, ['segunda lista', 90]]
>>> mi_lista.append('nuevo item')
>>> print (mi_lista)
['indice uno', 7, 9, 10, ['segunda lista', 90], 'nuevo item']
>>> 

#mi_lista.
#
#