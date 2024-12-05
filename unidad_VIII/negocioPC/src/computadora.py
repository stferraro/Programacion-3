from teclado import Teclado
from mouse import Mouse
from monitor import Monitor

class Computadora:
    
    contador_computadora = 0
    def __init__(self, teclado, mouse, monitor, costo):
        Computadora.contador_computadora += 1
        self.__id_computadora = Computadora.contador_computadora
        self.__teclado = teclado
        self.__mouse = mouse
        self.__monitor = monitor
        self.__costo = costo

    @property
    def _id_computadora(self):
        return self.__id_computadora

    @_id_computadora.setter
    def _id_computadora(self, value):
        self.__id_computadora = value

    @property
    def _teclado(self):
        return self.__teclado

    @_teclado.setter
    def _teclado(self, value):
        self.__teclado = value

    @property
    def _mouse(self):
        return self.__mouse

    @_mouse.setter
    def _mouse(self, value):
        self.__mouse = value

    @property
    def _monitor(self):
        return self.__monitor

    @_monitor.setter
    def _monitor(self, value):
        self.__monitor = value
        
    @property
    def _costo(self):
        return self.__costo

    @_costo.setter
    def _costo(self, value):
        self.__costo = value
        
    def costo_total_computadora(self):
        return self._costo + self._teclado._costo + self._mouse._costo + self._monitor._costo
        
    def __str__(self):
        return f"Computadora: {self._id_computadora} + Teclado: {self._teclado} + Mouse: {self._mouse} + Monitor: {self._monitor}"
