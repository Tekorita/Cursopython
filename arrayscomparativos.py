#Se le dan dos matrices de enteros a y b de la misma longitud, y un entero k. Estaremos iterando a través de la matriz a de izquierda a derecha, y simultáneamente a través de la matriz b de derecha a izquierda, y observaremos los pares (x, y), donde x ∈ a y y ∈ b. Tal par se llama minúsculo si la concatenación xy es estrictamente menor que k.

#Su tarea es devolver la cantidad de pares pequeños que encontrará durante la iteración simultánea a través de ay b.

#Ejemplo

#Para a = [1, 2, 3], b = [1, 2, 3] yk = 31, la salida debe ser
#countTinyPairs (a, b, k) = 2.

#Estamos considerando los siguientes pares durante la iteración:

#(1, 3). Su concatenación es igual a 13, que es menor que 31, por lo que el par es pequeño;
#(2, 2). Su concatenación es igual a 22, que es menor que 31, por lo que el par es pequeño;
#(3, 1). Su concatenación es igual a 31, que no es inferior a 31, por lo que el par no es muy pequeño.
#Como puede ver, hay 2 pares pequeños durante la iteración, por lo que la respuesta es 2.

#Para a = [16, 1, 4, 2, 14], b = [7, 11, 2, 0, 15] yk = 743, la salida debe ser
#countTinyPairs (a, b, k) = 4.

#Estamos considerando los siguientes pares durante la iteración:

#(16, 15). Su concatenación es igual a 1615, que es mayor que 743, por lo que el par no es pequeño;
#(1, 0). Su concatenación es igual a 10, que es menor que 743, por lo que el par es pequeño;
#(4, 2). Su concatenación es igual a 42, que es menos de 743, por lo que el par es pequeño.
#(2, 11). Su concatenación es igual a 211, que es menor que 743, por lo que el par es pequeño;
#(14, 7). Su concatenación es igual a 147, que es menos de 743, por lo que el par es pequeño.
#Hay 4 pares pequeños durante la iteración, por lo que la respuesta es 4.

a = [16,1,4,2,14]
b = [7,11,2,0,15]
k = 743

resultado = 0
for valor,valor2 in zip(a, b[::-1]):
    
    c = str(valor)+str(valor2)
    if int(c) < k:
        resultado = resultado + 1

print(resultado)




        

    
    