from utilidades.metaclases import MetaEntidad

class Persona(metaclass=MetaEntidad):

    def __init__(self, nombre, apellido, dni):

        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def mostrar_info(self):

        return f"{self.nombre} {self.apellido}"