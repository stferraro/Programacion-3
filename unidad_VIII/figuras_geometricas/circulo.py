import math
from figura_geometrica import FiguraGeometrica

class Circulo(FiguraGeometrica):
    
    def __init__(self, radio):
        self.__radio = radio

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, value):
        self.__radio = value
        
    def area(self):
        return (self.__radio ** 2) * math.pi
    
    def perimetro(self):
        return 2 * math.pi * self.__radio
    
    def __str__(self):
        return super().__str__() + f'\nRadio: {self.__radio} cm | Area: {self.area():.2f} cm^2 | Perimetro: {self.perimetro():.2f} cm' 
    


