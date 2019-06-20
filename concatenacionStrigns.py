#concatenacion de strings en python

my_string = "Hola mundo: 'David'"
my_string = 'Hola mundo: "David"'
course = 'Python 3'
name = 'David'

final_message1 = 'Nuevo curso o tutorial de:'+ course + ' por ' + name #1
final_message2 = 'Nuevo curso de %s por %s' %(course,name) #2
final_message3 = 'Nuevo curso de {} por {}' .format(course,name) #3

print(final_message3)
