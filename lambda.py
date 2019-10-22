#las lambdas son funciones anonymas sin nombre que se crean en una sola linea de codigo

#hacemos un ejemplo de una funcion normal

def suma(valor_uno, valor_dos):
	return valor_uno + valor_dos

resultado = suma(10,20)
print(resultado)

#ahora la convertimos en una funcion lambdas

#la estructura de una lambda es 1 los parametros o argumentos, 2 luego operacion o accion a ejecutar y por ultimo no necesitan return ya que siempre regresan algo

mi_funcion = lambda valor_uno, valor_dos : valor_uno + valor_dos #ejemplo lambda #1
formato = lambda sentencia : '{}?'.format(sentencia)
no_valor = lambda : 10
no_resultado = lambda : print('Deben de ejecutar una accion o proceso')

resultado = mi_funcion(2,2)
resultado2 = formato('Puedes hacer esto uno pregunta')

print(resultado2)

