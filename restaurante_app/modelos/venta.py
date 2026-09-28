class Venta:

    def __init__(
        self,
        usuario,
        producto,
        fecha
    ):

        self.usuario = usuario
        self.producto = producto
        self.fecha = fecha

    def __str__(self):

        return (
            f"{self.usuario} - "
            f"{self.producto} - "
            f"{self.fecha}"
        )