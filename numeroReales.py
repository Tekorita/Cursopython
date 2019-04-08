#Números reales
#En matemáticas, el conjunto de los números reales incluye a los números 
#racionales e irracionales. Un número real es positivo si es mayor que cero.
#El número cero es considerado número neutro. El resto de números serán 
#considerados negativos.

#En este ejercicio deberás programar un algoritmo encargado de diferenciar si 
#un número es positivo, negativo o neutro, e imprimir por la consola los mensajes
#"Es positivo", "Es negativo" o "Es neutro" respectivamente. Este proceso se 
#deberá repetir para cada una de los casos de prueba.

#Si te fijas en los casos de prueba, cada línea de las entradas se corresponde con
#la misma línea de las salidas, es decir, la primera línea de la entrada (cuyos
#valor es -1) se corresponde con la primera línea de la salida (cuyo valor es "Es
#negativo"), y así sucesivamente.

# Entradas y salidas
#Para cada línea de las entradas aparece 1 número real comprendido entre -10 y 10.
#Para cada línea de las entradas, las salidas deberán mostrar los casos 
#"Es negativo", "Es positivo" o "Es neutro".

#Casos de prueba

#Entrada    |   Salida
#-1         | Es negativo
# 0         | Es neutro
# 1         | Es Positivo 
i = 0
while i < 5:
    valor = float(input("Ingresa el valor a calcular please: "))

    if valor > 0:
        print("Es positivo")
    elif valor < 0:
        print("Es negativo")
    else:
        print("Es neutro")
    i = i + 1

