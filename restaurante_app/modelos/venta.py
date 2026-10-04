class Venta:

    def __init__(
        self,
        usuario: str,
        producto: str,
        fecha: str,
        cantidad: int = 1
    ) -> None:

        self.usuario = usuario
        self.producto = producto
        self.fecha = fecha
        self.cantidad = cantidad

    def __str__(self) -> str:
        return (
            f"{self.usuario} - "
            f"{self.producto} - "
            f"Cantidad: {self.cantidad} - "
            f"{self.fecha}"
        )
