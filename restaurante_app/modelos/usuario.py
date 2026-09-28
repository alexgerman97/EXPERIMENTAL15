class Usuario:

    def __init__(
        self,
        usuario: str,
        password: str,
        nombre: str
    ) -> None:

        self.usuario = usuario
        self.password = password
        self.nombre = nombre

    def __str__(self):

        return (
            f"{self.nombre} "
            f"({self.usuario})"
        )