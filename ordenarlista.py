lista = [0,6,2,2,5,4,3,1]
lista3 = []
print("lista desordenada: "+str(lista))
while lista != []:
    lista3.append(min(lista))
    lista.remove(min(lista))
    
print(lista)
