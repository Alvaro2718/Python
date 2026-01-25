

class Vehiculo:
    """Clase padre para este ejercicio que representa un vehículo"""

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Carro(Vehiculo):
    """Clase que representa un carro"""

    def __init__(self, marca, modelo, precio):
        super().__init__(marca, modelo)
        self.precio = precio


class Moto(Vehiculo):
    """Clase que representa una moto"""

    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada


class Camion(Vehiculo):
    """Clase que representa un camión"""

    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga


class Bicicleta(Vehiculo):
    """Clase que representa una bici"""

    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo


class Helicoptero(Vehiculo):
    """Clase extra para subir nota: Helicóptero"""

    def __init__(self, marca, modelo, altura_vuelo):
        super().__init__(marca, modelo)
        self.altura_vuelo = altura_vuelo


class Submarino(Vehiculo):
    """Clase extra para subir nota: Submarino"""

    def __init__(self, marca, modelo, profundidad):
        super().__init__(marca, modelo)
        self.profundidad = profundidad


carro = Carro("Toyota", "Corolla", 20000)
moto = Moto("Yamaha", "R3", 321)
camion = Camion("Volvo", "FH", 18000)
bici = Bicicleta("Trek", "Marlin 7", "Montaña")
helicoptero = Helicoptero("Pegasus", "H125", 6000)
submarino = Submarino("El del capitan Nemo", "S-81", 300)


print()
print("Carro  \nMarca:", carro.marca,
      "\nModelo:", carro.modelo,
      "\nPrecio:", carro.precio)
print()
print("Moto  \nMarca:", moto.marca,
      "\nModelo:", moto.modelo,
      "\nCilindrada:", moto.cilindrada)
print()
print("Camión  \nMarca:", camion.marca,
      "\nModelo:", camion.modelo,
      "\nCapacidad de carga:", camion.capacidad_carga, "kg")
print()
print("Bicicleta  \nMarca:", bici.marca,
      "\nModelo:", bici.modelo,
      "\nTipo:", bici.tipo)

print()
print("CLASES EXTRA PARA SUBIR NOTA AL 10")
print()
print("Helicóptero  \nMarca:", helicoptero.marca,
      "\nModelo:", helicoptero.modelo,
      "\nAltura de vuelo:", helicoptero.altura_vuelo, "metros")
print()

print("Submarino  \nMarca:", submarino.marca,
      "\nModelo:", submarino.modelo,
      "\nProfundidad máxima:", submarino.profundidad, "metros")
print()
