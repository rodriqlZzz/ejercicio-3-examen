class Car:
    num_cars = 0

    def __init__(self, marca, modelo, combustible, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.cilindrada = cilindrada
archivo = open('coches.txt','w')
archivo.write(self.marca)
archivo.write('\n')
archivo.write(self.modelo)
archivo.write('\n')
archivo.write(self.combustible)
archivo.write('\n')
archivo.write(self.cilindrada)
archivo.write('\n')
archivo.close()
