 #Mastermind

import random

continuar = 1

while continuar == 1:
	print("Bienvenido a youMasterMind")
	print("Elija la dificultad del juego <1=Easy, 2=Hard, 3=Hardcore>")
	dificultad = int(input("Digite el numero de dificultad: "))
	
	#ASignamos cantidad de digitos para cada dificultad

	if dificultad == 1:
		cant_digitos = 3
	elif dificultad == 2:
		cant_digitos = 4
	elif dificultad == 3:
		cant_digitos = 5

	digitos = ('0','1','2','3','4','5','6','7','8','9')
	codigo = ''

#Se selecciona los simbolos que formaran el codigo
	for i in range(cant_digitos):
		elegido = random.choice(digitos)
		while elegido in codigo:
			elegido = random.choice(digitos)	
		codigo = codigo = elegido

	print("Tienes que adivinar un codigo de ", cant_digitos, " Digitos distintos")
	propuesta = input("Que codigo propones?: ")

	intentos = 1

	while propuesta != codigo:
		intentos = intentos + 1
		aciertos = 0
		coincidencias = 0
		for i in range(cant_digitos):
			if propuesta[i] == codigo[i]:
				aciertos = aciertos + 1
			elif propuesta[i] in codigo:
				coincidencias = coincidencias + 1
		print("Tu propuesta(", propuesta, ") tiene ", aciertos, " aciertos y ", coincidencias, " coincidencias")
		propuesta = input("Propon otro codigo: ")

	print("Felicidades! adivinastes el codigo en ", intentos, " Intentos")
	continuar = int(input("Desea seguir juando? <1=si, 2=no>"))	