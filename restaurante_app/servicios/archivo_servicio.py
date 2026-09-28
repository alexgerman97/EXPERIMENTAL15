import json


class ArchivoServicio:

    def __init__(self) -> None:

        self.archivo_productos = (
            "restaurante_app/datos/productos.json"
        )

        self.archivo_usuarios = (
            "restaurante_app/datos/usuarios.json"
        )

        self.archivo_ventas = (
            "restaurante_app/datos/ventas.json"
        )

    def cargar_productos(self):

        try:

            with open(
                self.archivo_productos,
                "r",
                encoding="utf-8"
            ) as archivo:

                return json.load(archivo)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            return []

    def cargar_usuarios(self):

        try:

            with open(
                self.archivo_usuarios,
                "r",
                encoding="utf-8"
            ) as archivo:

                return json.load(archivo)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            return []

    def cargar_ventas(self):

        try:

            with open(
                self.archivo_ventas,
                "r",
                encoding="utf-8"
            ) as archivo:

                return json.load(archivo)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            return []

    def guardar_productos(
        self,
        productos
    ):

        with open(
            self.archivo_productos,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                productos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def guardar_ventas(
        self,
        ventas
    ):

        with open(
            self.archivo_ventas,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                ventas,
                archivo,
                indent=4,
                ensure_ascii=False
            )