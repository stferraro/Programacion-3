from figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, value):
        self.__lado = value

    def area(self):
        return self.__lado ** 2

    def perimetro(self):
        return self.__lado * 4

    def __str__(self):
        return super().__str__() + f'\nLado: {self.__lado} cm | Area: {self.area():.2f} cm^2 | Perimetro: {self.perimetro():.2f} cm'