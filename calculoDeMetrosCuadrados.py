#Cultivando habas en la huerta de Murcia
#Necesitamos plantar habas en un terreno de la huerta de Murcia. A la hora 
# de la siembra tenemos que dejar una separación de 50cm entre mata y mata 
# ya que cada una necesita un espacio de 0.25m2.

#En este ejercicio deberás programar un algoritmo encargado de calcular la 
# cantidad de habas que se pueden plantar en 5 terrenos cuadrados de la huerta
#  de Murcia conociendo la longitud o anchura de cada uno de ellos.

#Si te fijas en los casos de prueba, cada línea de las entradas se corresponde
#  con la misma línea de las salidas, es decir, la primera línea de la entrada
#  (cuyo valor es 1) se corresponde con la primera línea de la salida (cuyo valor
#  es 4), y así sucesivamente.

 #Entradas y salidas
#Las entradas estarán formadas por números reales comprendido entre 0 y 100.
#Las salidas deberán ser números naturales.

#Casos de prueba
#Entrada             Salida
#1           |       4
#2           |       16
#100         |       40000

i = 0

while i < 5:
    valor = float(input("Ingreso los metros del terreno"))
    resultado = valor * 4 * valor
    print(int(resultado))
    i = i + 1