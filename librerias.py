#las librerias son modulos predefinidos que vienen con python con diversas funciones

import random #nos permite trabajar con valores aleatorios
import datetime #nos permite trabajar con formatos de fecha y hora
import sys #nos permite trabajar con varias opciones de nuestro sistema
import time #nos permite trabajar con la libreria de tiempo y delay entre otras

valor = random.randint(0,10)#trae numeros aleatorios entre 0 y 10
lista = [True, "Strings", 23, False]
print(lista)
valor2 = random.choice(lista)#Tra valores aleatorios de la lista
print(valor2)
random.shuffle(lista)#Nos muestra la lista con sus atributos desordenados aleatoriamente
print(lista)

print(valor)

print(datetime.datetime.now())

#ahora hagamos un ejemplo usando la libreria sys

for i in range(100):
	time.sleep(0.2)
	sys.stdout.write("\r%d %%" % i)
	sys.stdout.flush()

for v in range(20):
	time.sleep(0.2)
	sys.stdout.write("\r%d %%" % i)
	sys.stdout.flush()
