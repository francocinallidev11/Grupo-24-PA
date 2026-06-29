import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utilidades.decoradores import registrar_accion

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

    # =========================================================================
    # GESTIÓN DE LIBROS
    # =========================================================================
    def listar_libros(self):
        return [libro.mostrar_info() for libro in self.libros]

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    @registrar_accion
    def agregar_libro(self, libro):
        if self.buscar_libro(libro.isbn) is not None:
            raise ValueError(f"Ya existe un libro con ISBN {libro.isbn}")
        self.libros.append(libro)

    @registrar_accion
    def eliminar_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro is None:
            raise ValueError(f"No existe un libro con ISBN {isbn}")
        self.libros.remove(libro)

    @registrar_accion
    def modificar_libro(self, isbn, **cambios):
        libro = self.buscar_libro(isbn)
        if libro is None:
            raise ValueError(f"No existe un libro con ISBN {isbn}")
        for atributo, valor in cambios.items():
            setattr(libro, atributo, valor)
        return libro

    # =========================================================================
    # GESTIÓN DE USUARIOS
    # =========================================================================
    def listar_usuarios(self):
        return [usuario.mostrar_info() for usuario in self.usuarios]

    def buscar_usuario(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario
        return None

    @registrar_accion
    def agregar_usuario(self, usuario):
        if self.buscar_usuario(usuario.dni) is not None:
            raise ValueError(f"Ya existe un usuario con DNI {usuario.dni}")
        self.usuarios.append(usuario)

    @registrar_accion
    def eliminar_usuario(self, dni):
        usuario = self.buscar_usuario(dni)
        if usuario is None:
            raise ValueError(f"No existe un usuario con DNI {dni}")
        self.usuarios.remove(usuario)

    @registrar_accion
    def modificar_usuario(self, dni, **cambios):
        usuario = self.buscar_usuario(dni)
        if usuario is None:
            raise ValueError(f"No existe un usuario con DNI {dni}")
        for atributo, valor in cambios.items():
            setattr(usuario, atributo, valor)
        return usuario



if __name__ == "__main__":
    def test_libros():
        from modelos.libro import Libro

        # DATOS PARA TESTS DE LIBROS
        libro1 = Libro("Cien años de soledad", "García Márquez", 1967 , "978-0307474728", 417)
        libro2 = Libro("Cien años de soledad: Edicion Limitada", "García Márquez", 2017 , "978-84-663-7971-7", 417)
        biblioteca = Biblioteca()
        
        # TEST AGREGAR LIBRO
        biblioteca.agregar_libro(libro1)
        biblioteca.agregar_libro(libro2)
        print("Test agregar_libro pasó correctamente")

        try:
            biblioteca.agregar_libro(libro1)
            print("Test agregar_libro con ISBN duplicado falló")
        except ValueError:
            print("Test agregar_libro con ISBN duplicado pasó correctamente")

        # TEST BUSCAR POR ISBN
        resultado = biblioteca.buscar_libro("978-0307474728")
        assert resultado == libro1, "El libro encontrado no coincide con el esperado"
        print("Test buscar_libro por ISBN pasó correctamente")

        resultado = biblioteca.buscar_libro("978-0307474710")
        assert resultado is None, "Se encontró un libro que no existe"
        print("Test buscar_libro por ISBN inexistente pasó correctamente")

        # TEST ELIMINAR LIBRO
        biblioteca.eliminar_libro("978-0307474728")
        print("Test eliminar_libro pasó correctamente")

        try:
            biblioteca.eliminar_libro("978-0307474728")
            print("Test eliminar_libro con ISBN inexistente falló")
        except:
            print("Test eliminar_libro con ISBN inexistente pasó correctamente")

        # TEST MODIFICAR LIBRO
        biblioteca.modificar_libro("978-84-663-7971-7", paginas=500)
        resultado = biblioteca.buscar_libro("978-84-663-7971-7")
        assert resultado.paginas == 500, "El número de páginas no se actualizó correctamente"
        print("Test modificar_libro pasó correctamente")

        try:
            biblioteca.modificar_libro("978-0307474728", paginas=300)
            print("Test modificar_libro con ISBN inexistente falló")
        except:
            print("Test modificar_libro con ISBN inexistente pasó correctamente")

        # TEST LISTAR LIBROS
        esperado = [(
            f"Cien años de soledad: Edicion Limitada - García Márquez (2017) "
            f"(ISBN: 978-84-663-7971-7, 500 págs.)"
        )]

        assert biblioteca.listar_libros() == esperado, "La lista de libros no coincide con la esperada"
        print("Test listar_libros pasó correctamente")

        print("Todos los tests de Biblioteca pasaron correctamente")
    
    def test_usuarios():
        from modelos.usuario import Usuario

        # DATOS PARA TESTS DE USUARIOS
        usuario1 = Usuario("Juan", "Pérez", "12345678A", "juan.perez@example.com")
        biblioteca = Biblioteca()

        # TEST AGREGAR USUARIO
        biblioteca.agregar_usuario(usuario1)
        print("Test agregar_usuario pasó correctamente")

        # TEST LISTAR USUARIOS
        esperado = [(
            f"Juan Pérez - juan.perez@example.com"
        )]
        assert biblioteca.listar_usuarios() == esperado, "La lista de usuarios no coincide con la esperada"
        print("Test listar_usuarios pasó correctamente")

        # TEST BUSCAR POR DNI
        resultado = biblioteca.buscar_usuario("12345678A")
        assert resultado == usuario1, "El usuario encontrado no coincide con el esperado"
        print("Test buscar_usuario por DNI pasó correctamente")

        # TEST MODIFICAR USUARIO
        biblioteca.modificar_usuario("12345678A", correo="juan.perez.updated@example.com")
        resultado = biblioteca.buscar_usuario("12345678A")
        assert resultado.correo == "juan.perez.updated@example.com", "El correo no se actualizó correctamente"
        print("Test modificar_usuario pasó correctamente")

        # TEST ELIMINAR USUARIO
        biblioteca.eliminar_usuario("12345678A")
        print("Test eliminar_usuario pasó correctamente")


    test_libros()
    test_usuarios()
