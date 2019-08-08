def superposicion(lista1, lista2):
    resultado = " "
    for valor1 in lista1:
        for valor2 in lista2:
            if valor1 == valor2:
                resultado = "True"                
            else:
                resultado = "False"
            
            print(resultado) 

list1 = [5,6,7,8]
list2 = [5,6,7,8]

superposicion(list1,list2)