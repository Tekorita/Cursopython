class autos_deportivos:

    def __init__(self, marca, modelo, ano, categoria, transmision, color, modo_compra, status = True):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.categoria = categoria
        self.transmision = transmision
        self.color = color
        self.status = status
        self.modo_compra = modo_compra

    def ver_datos(self):
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Ano: " + str(self.ano))
        print("Categoria: " + self.categoria)
        print("Transmision: " + self.transmision)
        print("Color: " + self.color)
        print("Modo de compra: " + self.modo_compra)

    def status_venta(self):
        return self.status

    def verificar_status(self):
        if self.status_venta():
            if (self.modo_compra == "credito") and (self.ano >=2017):
                print("Disponible su venta a credito por ser un coche nuevo o actual")
            else:
                print("Disponible su venta a contado recuerdo que aplica credito a carros del 2017 en adelante:)")
        else:
            print("El vehiculo ya ha sido vendido")

tuning = autos_deportivos('Chevrolet','corvette stingray',2018,'americanos', 'automatico','verde oliva','credito',False)

tuning.ver_datos()
tuning.verificar_status()

