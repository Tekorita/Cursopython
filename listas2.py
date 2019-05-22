my_list = ['strings', 15, 17.9, True, 'pera', 'manzana']
my_list.append(6)#agrega al final de la lista
my_list.insert(3, 'insert')#agrega en una posicion especifica
my_list.remove(15)#elimina registro de la lista
my_list.pop()#eliminar el ultimo registro en la lista

list_num = [50,8,3,20,15,2,1,4]
list_num2 = [70,80,90,100]
list_num.sort()#ordena numero de forma ascendente
list_num.sort(reverse = True)#ordena numero de forma desendente
list_num.append(list_num2)#agrega una lista dentro de otra
list_num.extend(list_num2)#concatena o una dos listas

print(my_list)
print(list_num)