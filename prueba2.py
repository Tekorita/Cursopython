lista1 = [1,2,3,4]
lista2 = [4,3,2,1]
lista3 = []
import pdb; pdb.set_trace()
print(lista1)
print(lista2)

for valor1, valor2 in zip(lista1,lista2):
    print(str(valor1)+" "+str(valor2)) 
    diccionario = {"libro":valor1}
    lista3.append(diccionario)

print(lista3)



