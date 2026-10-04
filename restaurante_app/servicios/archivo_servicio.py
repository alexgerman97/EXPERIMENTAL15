import json
from pathlib import Path


class ArchivoServicio:

    def __init__(self) -> None:
        self.base_dir = Path(__file__).resolve().parent.parent
        self.datos_dir = self.base_dir / "datos"

        self.archivo_productos = self.datos_dir / "productos.json"
        self.archivo_usuarios = self.datos_dir / "usuarios.json"
        self.archivo_ventas = self.datos_dir / "ventas.json"

        self.datos_dir.mkdir(exist_ok=True)

    def _cargar(self, ruta: Path) -> list:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos if isinstance(datos, list) else []
        except (FileNotFoundError, json.JSONDecodeError, PermissionError):
            return []

    def _guardar(self, ruta: Path, datos: list) -> None:
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )
        except PermissionError as error:
            raise PermissionError(
                f"No hay permisos para escribir en {ruta.name}."
            ) from error

    def cargar_productos(self) -> list:
        return self._cargar(self.archivo_productos)

    def cargar_usuarios(self) -> list:
        return self._cargar(self.archivo_usuarios)

    def cargar_ventas(self) -> list:
        return self._cargar(self.archivo_ventas)

    def guardar_productos(self, productos: list) -> None:
        self._guardar(self.archivo_productos, productos)

    def guardar_ventas(self, ventas: list) -> None:
        self._guardar(self.archivo_ventas, ventas)
