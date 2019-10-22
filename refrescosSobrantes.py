#Refrescos sobrantes en la fiesta del instituto
#Como te imaginarás, estamos organizando la fiesta de fin de curso de tu
#instituto y para ello tenemos que comprar latas de refrescos. Hemos pensado
#que la opción más económica es comprar cajas grandes las cuales contienen 
#12 latas por caja. Además, sabiendo que puede haber enfrentamientos entre 
#los alumnos, se ha decidido repartir los refrescos a partes iguales entre los
#alumnos de tal forma que todos deben beberse la misma cantidad de refrescos.

#En este ejercicio deberás programar un algoritmo encargado de calcular los 
#refrescos que sobrarán una vez repartidos en partes iguales entre todos los 
#alumnos. Para cada uno de los 5 casos de prueba te decimos la cantidad de cajas
#que se compran y el número de alumnos que asistirán a la fiesta.

#Si te fijas en los casos de prueba, cada línea de las entradas se corresponde 
#con la misma línea de las salidas, es decir, la primera línea de la entrada 
#(cuyos valores son 63 y 523) se corresponde con la primera línea de la salida 
#(cuyo valor es 233), y así sucesivamente.

# Entradas y salidas
#Para cada línea de las entradas aparecen 2 números naturales. El primero de ellos
#se corresponde con el número total de cajas de refrescos a comprar, y el segundo
#se corresponde al número total de alumnos que acudirán a la fiesta.
#Las salidas deberán ser números naturales correspondientes al número de refrescos
#sobrantes.
#Una vez programado pulsa el botón Comprobar automáticamente para comprobar que el
#código que has programado

#Casos de Prueba
#Entrada        |   Salida
#63 523         |   233
#85 624         |   396
#30 236         |   124
i = 0
while i < 5:
    cajas = int(input("Ingresa la cantidad de cajas de refrescos: "))
    alumnos = int(input("Ingresa la cantidad de alumnos a asistir: "))
    resultado = cajas * 12 - alumnos
    print(resultado)
    i = i + 1

