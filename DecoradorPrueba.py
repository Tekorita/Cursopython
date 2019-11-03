def decorador(func):
    def funcionB(*args):
        def antes():
            print("antes de la funcion")
        def despues():
            print("despues de la funcion")
        antes()
        resultado = func(*args)
        despues()
        return resultado
    return funcionB

@decorador
def sumas(valor1, valor2, valor3):
    calculo = valor1 + valor2 / valor3
    print(calculo)

@decorador
def restas(valor1, valor2, valor3):
    calculo = valor1 - valor2 / valor3
    print(calculo)

@decorador
def multiplicacion(valor1, valor2, valor3):
    calculo = valor1 * valor2 / valor3
    print(calculo)

valor1 = int(input("Ingresa el valor1: "))
valor2 = int(input("Ingresa el valor2: "))
valor3 = int(input("Ingresa el valor3: "))

sumas(valor1,valor2,valor3)
restas(valor1,valor2,valor3)
multiplicacion(valor1,valor2,valor3)

