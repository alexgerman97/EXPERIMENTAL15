class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> None:

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self) -> str:
        return (
            f"{self.codigo} - "
            f"{self.nombre} - "
            f"Stock: {self.stock}"
        )