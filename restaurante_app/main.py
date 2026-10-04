import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def main() -> None:
    root = tk.Tk()

    base_dir = Path(__file__).resolve().parent
    ruta_icono = base_dir / "assets" / "icono.ico"

    try:
        root.iconbitmap(ruta_icono)
    except tk.TclError as error:
        print(f"No se pudo cargar el icono: {error}")

    root.title("Restaurante App - Semana 15")
    root.geometry("1000x700")
    root.minsize(900, 650)

    archivo_servicio = ArchivoServicio()

    productos = archivo_servicio.cargar_productos()
    usuarios = archivo_servicio.cargar_usuarios()
    ventas = archivo_servicio.cargar_ventas()

    restaurante_servicio = RestauranteServicio(
        productos,
        usuarios,
        ventas
    )

    def mostrar_login() -> None:
        for widget in root.winfo_children():
            widget.destroy()

        LoginView(
            root,
            restaurante_servicio,
            mostrar_main
        )

    def mostrar_main() -> None:
        for widget in root.winfo_children():
            widget.destroy()

        MainView(
            root,
            restaurante_servicio,
            mostrar_login
        )

    mostrar_login()
    root.mainloop()


if __name__ == "__main__":
    main()
