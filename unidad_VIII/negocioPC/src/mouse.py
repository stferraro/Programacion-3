from dispositivo_entrada import DispositivoEntrada

class Mouse(DispositivoEntrada):
    
    contador_mouse = 0
    
    def __init__(self, marca , tipo_entrada, costo):
        Mouse.contador_mouse += 1
        self.__id_mouse = Mouse.contador_mouse
        self.__costo = costo
        super().__init__(marca, tipo_entrada)

    @property
    def _id_mouse(self):
        return self.__id_mouse

    @_id_mouse.setter
    def _id_mouse(self, value):
        self.__id_mouse = value

    @property
    def _costo(self):
        return self.__costo

    @_costo.setter
    def _costo(self, value):
        self.__costo = value
        
    def __str__(self):
        return f"Mouse: {self._id_mouse} + {super().__str__()} + Costo: {self._costo}"

        
        
    