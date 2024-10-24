class Materia:
    def __init__(self, codigo, nombre, nota, creditos):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__nota = nota
        self.__creditos = creditos
        
    @property
    def _codigo(self):
        return self.__codigo

    @_codigo.setter
    def _codigo(self, value):
        self.__codigo = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _nota(self):
        return self.__nota

    @_nota.setter
    def _nota(self, value):
        try:
            if value > 0 and value <= 20:
                self.__nota = value
        except ValueError:
            self.__nota = 0
    
    @property
    def _creditos(self):
        return self.__creditos

    @_creditos.setter
    def _creditos(self, value):
        try:
            if value > 0:
                self.__creditos = value
        except ValueError:
            self.__creditos = 0
        
    def __str__(self):
        return f'{self.__nombre} {self.__nota} {self.__creditos} {self.__codigo}'

        
    
    