from computadora import Computadora

class Orden:
    contador_orden = 0

    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self.__id_orden = Orden.contador_orden
        self.__computadoras = computadoras

    @property
    def _id_orden(self):
        return self.__id_orden

    @_id_orden.setter
    def _id_orden(self, value):
        self.__id_orden = value

    @property
    def _computadoras(self):
        return self.__computadoras

    @_computadoras.setter
    def _computadoras(self, value):
        self.__computadoras = value
        
    def add_computadora(self, computadora):
        self.__computadoras.append(computadora)
        
    def remove_computadora(self, computadora):
        self.__computadoras.remove(computadora)
        
    def search_computadora(self, id_computadora):
        for computadora in self.__computadoras:
            if computadora._id_computadora == id_computadora:
                return computadora
            else :
                raise Exception("Computadora no encontrada")
        return None
    
    def costo_total_orden(self):
        costo_total = 0
        for computadora in self.__computadoras:
            costo_total += computadora.costo_total_computadora()
        return costo_total
    
    def print_costo(self):
        return f"Orden: {self._id_orden} + Costo: {self.costo_total_orden():.2f}"
    
    def __str__(self):
        computadoras_str = [str(computadora) for computadora in self.__computadoras]
        return f"Orden: {self._id_orden} + Computadoras: {computadoras_str}"
    
    def create_txt(self, nombre_archivo):
        with open(f"{nombre_archivo}.txt", "w") as file:
            file.write(self.__str__() + "\n" + self.print_costo())  

        