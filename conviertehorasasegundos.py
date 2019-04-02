#Convierte de horas a segundos
#En este ejercicio deberás programar un algoritmo encargado de convertir una
#determinada cantidad de horas a segundos. Para ello deberás programar el 
# código necesario que solicite al usuario que introduzca 5 números (horas) 
# e imprima por la consola la conversión a segundos.

#Si te fijas en los casos de prueba, cada línea de las entradas se corresponde 
# con la misma línea de las salidas, es decir, la primera línea de los casos de 
# prueba (cuyo valor es 1) se corresponde con la primera línea de la salida 
# (cuyo valor es 3600), y así sucesivamente.

#Las entradas estarán formadas por números reales comprendido entre 0 y 100.
#Las salidas deberán ser números naturales.

#Casos de prueba
#entrada | salida
#1       |3600
#1.5     |5400
#2       |7200

i = 0

while i < 5:
    valor = float(input("ingresa una hora por favor"))
    resultado = valor * 3600
    print(int(resultado))
    i = i + 1

