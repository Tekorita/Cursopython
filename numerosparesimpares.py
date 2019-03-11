lista = range(1,11)

for valor in lista:
	resultado = valor % 2
	if resultado == 0:
		print(valor)
		
lista_pares = [valor for valor in range(0, 11) if valor % 2 == 0 ]

print(lista_pares)