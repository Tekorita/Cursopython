#Los metodos de clase son metodos que le pertenezen a la clase sin necesidad de crear objetos

class Animal:
	volador = True

class Cocodrilo(Animal):

	def __init__(self, nombre):
		self.nombre = nombre

#para que un metodo sea propio de una clase tengo que usar el @ como si fuera un decorador
#La diferencia de usar un metodo de clase con un metodo estatico es que pueden acceder a los atributos o metodos de las clases que estamos heredando
#por ejemplo en la classmethon puedo acceder al atributo que hereda cocodrilo de animal que seria volador = False

#en conclusion los metodos estaticos le pertenecen solo a las clases y los metodos de clase le pertenecen a las clases y tambien pueden utilizar atributos publicos y los metodos publicos de las clases padre
	@classmethod
	def new(cls, nombre):
		cls.volador = False
		return Cocodrilo(nombre)



cocodrilo = Cocodrilo.new('coco')
print(cocodrilo.nombre)
print(cocodrilo.volador)
