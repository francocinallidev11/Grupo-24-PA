from utilidades.metaclases import MetaEntidad
from utilidades.validadores import validar_isbn

class Libro(metaclass=MetaEntidad):
    def __init__(self, titulo, autor, isbn, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn      # pasa por el setter -> valida
        self.paginas = paginas

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, valor):
        if not validar_isbn(valor):
            raise ValueError(f"ISBN inválido: {valor}")
        self._isbn = valor

    def mostrar_info(self):
        return (
            f"{self.titulo} - {self.autor} "
            f"(ISBN: {self.isbn}, {self.paginas} págs.)"
        )
