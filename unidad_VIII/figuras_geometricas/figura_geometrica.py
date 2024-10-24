from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass
    
    def __str__(self):
        return 'Figura geometrica'