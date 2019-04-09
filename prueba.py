def generador(*args):
    for valor in args:
        yield valor * 1
lista=[0]
for valor1 in generador(1,2,3,4,5,6,7,8,9,10):
    lista[valor1] = valor1

print(lista)