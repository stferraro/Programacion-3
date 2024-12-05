class Monitor :
    
    contador_monitor = 0
    
    def __init__(self, marca, pulgadas , costo):
        Monitor.contador_monitor += 1
        self.__id_monitor = Monitor.contador_monitor
        self.__marca = marca
        self.__pulgadas = pulgadas
        self.__costo = costo

    @property
    def _id_monitor(self):
        return self.__id_monitor

    @_id_monitor.setter
    def _id_monitor(self, value):
        self.__id_monitor = value

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

    @property
    def _pulgadas(self):
        return self.__pulgadas

    @_pulgadas.setter
    def _pulgadas(self, value):
        self.__pulgadas = value

    @property
    def _costo(self):
        return self.__costo

    @_costo.setter
    def _costo(self, value):
        self.__costo = value
        
    def __str__(self):
        return f"Monitor: {self._id_monitor} + Marca: {self._marca} + Pulgadas: {self._pulgadas} + Costo: {self._costo}"
