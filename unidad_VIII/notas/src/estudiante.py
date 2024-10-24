class Estudiante:
    
    def __init__(self, nombre, apellido, cedula, sexo, codigo, materias):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__sexo = sexo
        self.__codigo = codigo
        self.__materias = materias

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value

    @property
    def _sexo(self):
        return self.__sexo

    @_sexo.setter
    def _sexo(self, value):
        self.__sexo = value

    @property
    def _codigo(self):
        return self.__codigo

    @_codigo.setter
    def _codigo(self, value):
        self.__codigo = value

    @property
    def _materias(self):
        return self.__materias

    @_materias.setter
    def _materias(self, value):
        self.__materias = value
        
    def agrega_materia(self, materia):
        self.__materias.append(materia)
        
    def elimina_materia(self, materia):
        self.__materias.remove(materia)
        
    def busca_materia(self, codigo):
        for materia in self.__materias:
            if materia._codigo == codigo:
                return True
        return False
    
    def __str__(self):
        datos_estudiante = f'{self._nombre} {self._apellido} {self._cedula} {self._sexo} {self._codigo}'
        materias_str = ''
        for materia in self.__materias:
            materias_str += f'{materia} '
        return f'{datos_estudiante} {materias_str}'
    

        
    