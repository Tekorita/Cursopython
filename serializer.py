import marshal

lista = [1,2,3,4,5]

serializado = marshal.dumps(lista)

print(serializado)

deserializado = marshal.loads(serializado)

print(deserializado)

