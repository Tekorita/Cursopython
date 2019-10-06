#modo tradicional para llenar una lista con for

"""lista = [] #false
for valor in range(0,101):
	lista.append(valor)

print(lista)"""

#llenar una lista con list comprehension

lista = [valor for valor in range(0, 101)]

print(lista)

lista_pares = [valor for valor in range(0, 101) if valor % 2 == 0 ]
lista_2 = [valor for valor in range(0, 101) if valor % 2 == 0 ]
lista_3 = [valor for valor in range(0, 101) if valor % 2 == 0 ]

print(lista_pares)

#luego las listas comprehension se pueden utilizar para llenar tuplas 

tupla = tuple((valor for valor in range(0, 101) if valor % 2 != 0))

print(tupla)

#Por ultimo las listas comprehension se pueden utilizar para llenar Diccionarios 

diccionario = { indice:valor for indice, valor in enumerate(lista) if indice < 10}

print(diccionario)