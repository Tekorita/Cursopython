# import re
# cadena = "Esto Es Un EjemplO"
# expresion = re.compile(r'[A-Z]')
# caracter= r"\L0"

# def reemplazar_mayusculas(cadena, expresion, caracter):

#     expresion=expresion.sub(caracter, cadena)
#     print(expresion)

# reemplazar_mayusculas(cadena, expresion, caracter)

var pattern: RegExp;
var str: String = "HI guys";
pattern = /([A-Z]+)/g;
str = str.replace(pattern, thisShouldBeLowerCase);