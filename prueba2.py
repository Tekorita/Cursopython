class Animal:
    volador = True

class Cocodrilo(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def mostrar_datos(cls, nombre):
        cls.volador = False
        return Cocodrilo(nombre)

cocodril = Cocodrilo.mostrar_datos("rabioso")

print(cocodril.volador)
print(cocodril.nombre)

            
