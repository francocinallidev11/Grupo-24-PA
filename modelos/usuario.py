from modelos.persona import Persona


class Usuario(Persona):

    def __init__(
        self,
        nombre,
        apellido,
        dni,
        correo
    ):
        # Invocamos al constructor de la clase padre (Persona)
        super().__init__(
            nombre,
            apellido,
            dni
        )
        self.correo = correo

    def mostrar_info(self):
        # Comportamiento polimórfico requerido por MetaEntidad
        return (
            f"{self.nombre} "
            f"{self.apellido} "
            f"- {self.correo}"
        )
