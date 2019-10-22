import marshal

lista = [1,2,3,4,5,6,7,8,9]

serializado = marshal.dumps(lista)

print(serializado)

deserializado = marshal.loads(serializado)
deserializado2 = marshal.loads(serializado)

print(deserializado)

