#print("qA2".isalnum())
#print("qA2".isalpha())
#print("qA2".isdigit())
#print("qA2".islower())
#print("qA2".isupper())

s = "qA2"

def is_num(text):
    resultado = 'False'
    for a in s:
        if a.isalnum():
            resultado = 'True'

    print(resultado)

def is_alpha(text):
    resultado = 'False'
    for a in s:
        if a.isalpha():
            resultado = 'True'

    print(resultado)

def is_digit(text):
    resultado = 'False'
    for a in s:
        if a.isdigit():
            resultado = 'True'

    print(resultado)

def is_lower(text):
    resultado = 'False'
    for a in s:
        if a.islower():
            resultado = 'True'

    print(resultado)

def is_upper(text):
    resultado = 'False'
    for a in s:
        if a.isupper():
            resultado = 'True'

    print(resultado)

is_num(s)
is_alpha(s)
is_digit(s)
is_lower(s)
is_upper(s)