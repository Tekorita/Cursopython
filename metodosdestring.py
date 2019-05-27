course = 'Curso de platzi o merojandola'
my_string = 'Codigo Facilito plus'

"""Metodos de formato"""
result = '{a} de {b}'.format(a=course, b=my_string)
#result = result.lower()#minusculas
#result = result.upper()#mayusculas
#result = result.title()#titulo

"""Metos de busqueda"""
pos = result.find('Codigo')#busca la posicion en la que se encuentra el caracter
count = result.count('o')#busca cuantas veces se repite un caracter

"""Metodos de sustitucion"""
new_string = result.replace('o','x')#remplace un caracter por otro
new_string = result.split(' ')#combierte el string en una lista apartir de donde haya un espacio


print(new_string)