#https://www.w3schools.com/python/python_regex.asp

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
#x = re.search("^The.*Spain$", txt)
x = re.search("^The", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")


#Funciones RegEx
#El remódulo ofrece un conjunto de funciones que nos permite buscar una cadena para una coincidencia:
#
#     findall     Devuelve una lista que contiene todas las coincidencias
#     search      Devuelve un objeto Match si hay una coincidencia en cualquier lugar de la cadena
#     split       Devuelve una lista donde la cadena se ha dividido en cada coincidencia
#     sub         Reemplaza una o varias coincidencias con una cadena


#Metacaracteres
#Los metacaracteres son caracteres con un significado especial:
#
#     [] Un conjunto de caracteres "[a-m]"
#     \ Señala una secuencia especial (también se puede usar para escapar de caracteres especiales) "\ d"
#     . Cualquier carácter (excepto el carácter de nueva línea) "he..o"
#     ^ Comienza con "^ hola"
#     $ Termina con "mundo $"
#     * Cero o más ocurrencias "aix *"
#     + Una o más ocurrencias "aix +"
#     {} Exactamente el número especificado de ocurrencias "al {2}"
#     El | O bien "cae | se queda"
#     () Captura y grupo


#Secuencias especiales
#Una secuencia especial es \seguida por uno de los caracteres en la lista a continuación y tiene un significado especial:
# 
#     \A  Devuelve una coincidencia si los caracteres especificados están al principio de la cadena     "\ AThe"
#     \b  Devuelve una coincidencia donde los caracteres especificados están al principio o al final de una palabra       r "\ bain"       r "ain \ b"
#     \B  Devuelve una coincidencia donde los caracteres especificados están presentes, pero NO al principio (o al final) de una palabra      r "\ Bain"      r "ain \ B"
#     \d  Devuelve una coincidencia donde la cadena contiene dígitos (números del 0-9)       "\ d"
#     \D  Devuelve una coincidencia donde la cadena NO contiene dígitos       "\ D"
#     \s  Devuelve una coincidencia donde la cadena contiene un espacio en blanco         "\ s"
#     \S  Devuelve una coincidencia donde la cadena NO contiene un espacio en blanco      "\ S"
#     \w  Devuelve una coincidencia donde la cadena contiene caracteres de palabras (caracteres de la A a la Z, dígitos del 0 al 9 y el carácter de subrayado _)       "\ w"
#     \W  Devuelve una coincidencia donde la cadena NO contiene ningún carácter de palabra      "\ W"
#     \Z  Devuelve una coincidencia si los caracteres especificados están al final de la cadena         "España \ Z"


#Conjuntos
#Un conjunto es un conjunto de caracteres dentro de un par de corchetes []con un significado especial:
#
#     [arn]    Devuelve una coincidencia donde está presente uno de los caracteres especificados (a, r o n)
#     [a-n]    Devuelve una coincidencia para cualquier carácter en minúscula, alfabéticamente entre a y n
#     [^ arn]    Devuelve una coincidencia para cualquier carácter EXCEPTO a, r y n
#     [0123]    Devuelve una coincidencia donde cualquiera de los dígitos especificados (0, 1, 2 o 3) están presentes
#     [0-9]    Devuelve una coincidencia para cualquier dígito entre 0 y 9
#     [0-5] [0-9]    Devuelve una coincidencia para cualquier número de dos dígitos del 00 y 59
#     [a-zA-Z]    Devuelve una coincidencia para cualquier carácter alfabéticamente entre a y z, minúsculas O mayúsculas
#     [+]    En conjuntos, +, *,., |, (), $, {} No tiene un significado especial, por lo que [+] significa: devolver una coincidencia para cualquier carácter + en la cadena


#------------------------------------------------------------------------------------------------------------------------------

#Ejemplo con findall() La findall()función devuelve una lista que contiene todas las coincidencias.
#La lista contiene las coincidencias en el orden en que se encuentran.
print("- findall")
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

#Devuelve una lista vacía si no se encontró ninguna coincidencia:
print("findall()")
str = "The rain in Spain"
x = re.findall("Portugal", str)
print(x)

#------------------------------------------------------------------------------------------------------------------------------

#Ejemplo con search() La search()función busca una coincidencia en la cadena y devuelve un objeto Match si hay una coincidencia.
#Si hay más de una coincidencia, solo se devolverá la primera aparición de la coincidencia:
print("- search")
str = "The rain in Spain"
x = re.search("\s", str) # \n quiere decir espacio en blanco

print("The first white-space character is located in position:", x.start())

#Si no se encuentran coincidencias, Nonese devuelve el valor :
print("- search")
str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)

#------------------------------------------------------------------------------------------------------------------------------

#Ejemplo con split(), La split()función devuelve una lista donde la cadena se ha dividido en cada coincidencia:
#Ejemplo
#Dividir en cada carácter de espacio en blanco:
print("- split")
str = "The rain in Spain"
x = re.split("\s", str)
print(x)

#Puede controlar el número de ocurrencias especificando el maxsplit parámetro:
print("- split")
str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)

#------------------------------------------------------------------------------------------------------------------------------

#Ejemplo con la funcion sub() La sub() función reemplaza las coincidencias con el texto de su elección:

#Ejemplo
#Reemplace cada carácter de espacio en blanco con el número 9:
print("- sub")
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

#Puede controlar el número de reemplazos especificando el count parámetro:
print("- sub")
str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)

#------------------------------------------------------------------------------------------------------------------------------

#Match Object
#Un objeto de coincidencia es un objeto que contiene información sobre la búsqueda y el resultado.

#Nota: Si no hay coincidencia, Nonese devolverá el valor , en lugar del Objeto de coincidencia.

#Ejemplo
#Haga una búsqueda que devolverá un objeto de coincidencia:

str = "The rain in Spain"
x = re.search("ai", str)
print(x) #this will print an object

#El objeto Match tiene propiedades y métodos utilizados para recuperar información sobre la búsqueda y el resultado:

#.span()devuelve una tupla que contiene las posiciones inicial y final del partido. 
#.stringdevuelve la cadena pasada a la función 
#.group()devuelve la parte de la cadena donde hubo una coincidencia

#Ejemplo
#Imprima la posición (posición inicial y final) de la primera aparición de coincidencia.

#La expresión regular busca cualquier palabra que comience con una mayúscula "S":
print("- Match -span")
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())

#Imprima la cadena pasada a la función:
print("- Match -strings")
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.string)

#Ejemplo
#Imprima la parte de la cadena donde hubo una coincidencia.

#La expresión regular busca cualquier palabra que comience con una mayúscula "S":
print("- Match -group")
str = "The rain in Spain and Mexico"
x = re.search(r"\bS\w+", str)
print(x.group())
#Nota: Si no hay coincidencia, Nonese devolverá el valor , en lugar del Objeto de coincidencia.