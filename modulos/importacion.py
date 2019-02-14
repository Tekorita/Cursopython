#Existen varias formas de importar funciones de un modulo

import calculos #forma 1

calculos.suma()
calculos.resta()

#from calculos import suma, resta #forma 2
##from calculos import division as div #forma 3
#from calculos import suma, resta, multiplicacion #forma 4
#from calculos import * #forma 5 para importar todas las funciones del modulo

#resultado = suma(2, 2)
#print(resultado)

print(__name__) #el atributo __name__ es para determinar que script o archivo sea el principal de ser el principal su valor sera __main__



