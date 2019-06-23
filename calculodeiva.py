#IVA de los productos
#El IVA es un Impuesto sobre el Valor Añadido de un servicio o producto. 
# En España disponemos de varios tipos de IVA como el 21%, 10% y 4%. 
# Este impuesto grava sobre el precio neto del producto, es decir, el precio
# total o bruto corresponde al precio neto del producto más el impuesto que 
# se le aplica.

#En este ejercicio deberás programar un algoritmo encargado de calcular el 
# precio bruto para 5 productos (conociendo el precio neto y el IVA aplicado).

#Si te fijas en los casos de prueba, cada línea de las entradas se corresponde
#con la misma línea de las salidas, es decir, la primera línea de la entrada 
#(cuyos valores son 100 y 21) se corresponde con la primera línea de la salida 
#(cuyo valor es 121), y así sucesivamente.

# Entradas y salidas
#Para cada línea de las entradas aparecen dos números naturales. 
# El primero de ellos corresponde al precio neto del producto y contendrá 
# un número comprendido entre 0 y 100. El segundo número se corresponde 
# con el IVA del producto que tomará los valores 21, 10 ó 4.
#Las salidas deberán ser números reales.

# Casos de prueba
#Entradas        Salidas
#100 21       | 121
#50 10        | 55
#25 4         | 26

i = 0

while i < 5:
    precio = int(input("ingresa el precio: "))
    impuesto = int(input("ingresa el impuesto: "))
    resultado = precio * impuesto / 100 + precio
    print(float(resultado))
    i = i + 1

