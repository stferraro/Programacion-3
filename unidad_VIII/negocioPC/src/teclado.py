from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    
    contador_teclado = 0
    
    def __init__(self, marca , tipo_entrada, costo):
        Teclado.contador_teclado += 1
        self.__id_teclado = Teclado.contador_teclado
        self.__costo = costo
        super().__init__(marca, tipo_entrada)
    @property
    def _id_teclado(self):
        return self.__id_teclado

    @_id_teclado.setter
    def _id_teclado(self, value):
        self.__id_teclado = value

    @property
    def _costo(self):
        return self.__costo

    @_costo.setter
    def _costo(self, value):
        self.__costo = value
        
    def __str__(self):
        return f"Teclado: {self._id_teclado} + {super().__str__()} + Costo: {self._costo}"