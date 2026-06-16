from utilidades.metaclases import MetaEntidad

class Libro(metaclass=MetaEntidad):

    def __init__(
        self,
        titulo,
        autor,
        isbn,
        paginas
    ):

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.paginas = paginas

    def mostrar_info(self):

        return (
            f"{self.titulo} - "
            f"{self.autor}"
        )
