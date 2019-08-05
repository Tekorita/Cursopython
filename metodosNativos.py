lista = [1,1,1,3,3,4,4,4,4,5]



def migratoryBirds(arr):
    lista2 = list(set(arr))
    resultado = [] 
    for valor in lista2:
        resultado.append(arr.count(valor))
    
    print(arr)
    print(lista2)
    print(resultado)

migratoryBirds(lista)

#print(lista2)
#print(lista)

#print(lista.count(5))