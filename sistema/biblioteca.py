class Biblioteca:

    _instancia = None

    def __new__(cls):

        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

        return cls._instancia

    def __init__(self):

        if not hasattr(self, "_inicializado"):

            self.libros = []
            self.usuarios = []
            self.prestamos = []

            self._inicializado = True