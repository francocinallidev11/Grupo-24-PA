from datetime import date

class Prestamo:

    def __init__(
        self,
        libro,
        usuario
    ):

        self.libro = libro
        self.usuario = usuario

        self.fecha_prestamo = date.today()

        self.fecha_devolucion = None

        self.activo = True

    def devolver(self):

        self.fecha_devolucion = date.today()

        self.activo = False

    def mostrar_info(self):

        return (
            f"{self.libro.titulo} "
            f"prestado a "
            f"{self.usuario.nombre}"
        )