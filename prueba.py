def tablaDeMultiplicar(valor):
    for num in range(1,11):
        resultado = valor * num
        print(str(valor)+" x "+str(num)+" = "+str(resultado))

valor1 = int(input("Ingresa el numero de la tabla de multiplicar"))
tablaDeMultiplicar(valor1)
