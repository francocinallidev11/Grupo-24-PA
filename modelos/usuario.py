from modelos.persona import Persona


class Usuario(Persona):

    def __init__(
        self,
        nombre,
        apellido,
        dni,
        correo
    ):
        super().__init__(
            nombre,
            apellido,
            dni
        )
        self.correo = correo

    def mostrar_info(self):
        return (
            f"{self.nombre} "
            f"{self.apellido} "
            f"- {self.correo}"
        )
