palabra = input(str("ingresa una palabra o oracion que sea palindromo: "))

palabra = palabra.replace(" ","")

if palabra == palabra[::-1]:
    print("esta palabra es un palindromo")
else:
    print("esta palabra no es un palindromo")