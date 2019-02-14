Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> mi_lista = ["python","java","C++","PHP","Ruby",]
>>> for lenguaje in mi_lista: #por cada lenguaje de mi mi_lista
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block
>>> for lenguaje in mi_lista: #por cada lenguaje de mi mi_lista
... 	print(lenguaje)
... 
python
java
C++
PHP
Ruby
>>> 
>>> for edad in range (10, 18):
... 	print("tu edad es: ", edad)
... 
tu edad es:  10
tu edad es:  11
tu edad es:  12
tu edad es:  13
tu edad es:  14
tu edad es:  15
tu edad es:  16
tu edad es:  17
>>> tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> multiplicar = int(input("QUe tabla de multiplicar desea?"))
QUe tabla de multiplicar desea?9
>>> for numero in tabla:
... 	print(multiplicar, " x ", numero, " = ", multiplicar*numero)
... 
9  x  1  =  9
9  x  2  =  18
9  x  3  =  27
9  x  4  =  36
9  x  5  =  45
9  x  6  =  54
9  x  7  =  63
9  x  8  =  72
9  x  9  =  81
9  x  10  =  90
>>> 