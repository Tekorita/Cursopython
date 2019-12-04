diccionario = { 'a' : 55, 67 : 'valor rico', 80: True, 'a': 90, 'lastvalue' : 900 }#Las claves o llaves tienen que ser inmutables
#si se colocan llaves con el mismo nombre se reflejara la ultima llave o clave
print(diccionario)

diccionario[67] = 'Chetaa da moraaaa'

edad_abuela = diccionario['a']
busqueda = diccionario.get(68,'no se encontro la chetaaa') #obtenemos valores

llaves_diccionario = diccionario.keys() #obtenemos solo las llaves del diccionario

del diccionario['lastvalue'] #del nos ayuda a eliminar una llave

llaves_lista = list(diccionario.keys()) #mostramos las llaves del diccionario como una lista 
valores_lista = list(diccionario.values()) #mostramos los valores del diccionario como una lista 

llaves_tuplas = tuple(diccionario.keys()) #mostramos las llaves del diccionario como una tupla 
valores_tuplas = tuple(diccionario.values()) #mostramos los valores del diccionario como una tupla 
"""como concatenar diccionarios existen 2 formas"""

diccionario2 = {9 : 'ronaldo CR7', 10: 'messi', 7: 'ibrahimobich'}

diccionario['a']= diccionario2[9]
diccionario[67]= diccionario2[10]

diccionario.update(diccionario2)

print(diccionario)

print(edad_abuela)

print(busqueda)

print(llaves_diccionario)

print(llaves_lista)

print(llaves_lista[1])

