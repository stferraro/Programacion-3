from figura_geometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def _base(self):
        return self.__base

    @_base.setter
    def _base(self, value):
        self.__base = value

    @property
    def _altura(self):
        return self.__altura

    @_altura.setter
    def _altura(self, value):
        self.__altura = value
        
    def area(self):
        return (self._base * self._altura) / 2
    
    def perimetro(self):
        return (self._base * 2) + (self._altura * 2)
    
    def __str__(self):
        return super().__str__() + f'\nBase: {self._base} cm | Altura: {self._altura} cm | Area: {self.area():.2f} cm^2 | Perimetro: {self.perimetro():.2f} cm'

        
    