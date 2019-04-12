import marshal

lista = [1]

serializado = marshal.dumps(lista)

print(serializado)

deserializado = marshal.loads(serializado)

print(deserializado)

