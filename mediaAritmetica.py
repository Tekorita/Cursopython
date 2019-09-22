#Calculando la media aritmética
#En matemáticas, la media aritmética de un conjunto de números es el valor
#que se obtiene a partir de la suma de varios números dividido entre el
#número de sumandos.

#En este ejercicio deberás programar un algoritmo encargado de calcular 5 medias
#aritméticas, a partir de 4 números dados.

#Si te fijas en los casos de prueba, cada línea de las entradas se corresponde con
#la misma línea de las salidas, es decir, la primera línea de la entrada (cuyos 
#valores son 2, 4, 6 y 8) se corresponde con la primera línea de la salida (cuyo
#valor es 5), y así sucesivamente.

# Entradas y salidas
#Para cada línea de las entradas aparecen 4 números naturales.
#Las salidas deberán ser números reales.

#Casos de prueba
#Entrada            Salida
#2 4 6 8        |   5
#8 5 20 7       |   10
#12 6 18 4      |   10

i = 0
x = 0
lista = [4,0,6,0]
numero2 = 0

while x < 2:
    while i < 4:
        valor = int(input("Ingresa el valor para hacer el calculo o procedimiento"))
        lista[i] = valor
        i = i + 1

    for numero in lista:
        numero2 = numero + numero2 

    resultado = numero2 / 4
    print(float(resultado))
    x = x + 1
    i = 0
    resultado = 0
    numero = 0
    numero2 = 0
    

