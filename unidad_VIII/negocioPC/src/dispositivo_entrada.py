class DispositivoEntrada:
    
    def __init__(self, marca , tipo_entrada):
        self.__marca = marca
        self.__tipo_entrada = tipo_entrada
        
    def __str__(self):
        return f"Marca: {self.__marca}, Tipo Entrada: {self.__tipo_entrada}"