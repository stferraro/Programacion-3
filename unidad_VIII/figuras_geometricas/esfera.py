from figura_geometrica import FiguraGeometrica
import math

class Esfera(FiguraGeometrica):
    
    def __init__(self, radio):
        self.__radio = radio
        
    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, value):
        self.__radio = value
        
    def area(self):
        return 4 * math.pi * (self.__radio ** 2)
    
    def perimetro(self):
        return 4 * math.pi * self.__radio
    
    def volumen(self):
        return (4 / 3) * math.pi * (self.__radio ** 3)
    
    def __str__(self):
        return super().__str__() + f'\nRadio: {self.__radio} cm | Area: {self.area():.2f} cm^2 | Perimetro: {self.perimetro():.2f} cm | Volumen: {self.volumen():.2f} cm^3'