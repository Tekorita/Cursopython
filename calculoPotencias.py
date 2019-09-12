#Calculando potencias
#La potencia de un número multiplica a dicho número por sí mismo tantas veces
#como indique el exponente.

#En este ejercicio deberás programar un algoritmo encargado de calcular la potencia
#de un número conociendo su exponente e imprimir el resultado por la consola. 
# Este proceso se deberá repetir para cada uno de los casos de prueba.

#Si te fijas en los casos de prueba, cada línea de las entradas se corresponde 
# con la misma línea de las salidas, es decir, la primera línea de la entrada 
# (cuyos valores son 2 y 3) se corresponde con la primera línea de la salida 
# (cuyo valor es 8), y así sucesivamente.

# Entradas y salidas
#Para cada línea de las entradas aparecen dos números naturales comprendidos 
#entre 0 y 10. El primero de ellos corresponde a la base y el segundo al exponente
#de la potencia.
#Las salidas deberán ser números naturales.
#Una vez programado pulsa el botón Comprobar automáticamente para comprobar que el
#código que has programado es correcto.

#Casos de prueba
#Entrada        |   Salida
#2 3            |   8
#4 6            |   4096
#6 3            |   216
x = 0
i = 0
resultado = 1
while i < 5:
    valor = int(input("ingresa el valor base o inicial: "))
    exponente = int(input("ingresa el exponente: "))

    while x < exponente:
        resultado = valor * resultado
        x = x +1

    print(resultado)
    resultado = 1
    x = 0
    i = i + 1

