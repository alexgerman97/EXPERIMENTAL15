import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio

from ui.login_view import LoginView
from ui.main_view import MainView


def main() -> None:

    root = tk.Tk()

    try:
        root.iconbitmap("assets/icono.ico")
    except Exception as e:
        print("Error icono:", e)

    root.title("Restaurante App")
    root.geometry("900x600")

    archivo_servicio = ArchivoServicio()

    productos = (
        archivo_servicio.cargar_productos()
    )

    usuarios = (
        archivo_servicio.cargar_usuarios()
    )

    ventas = (
        archivo_servicio.cargar_ventas()
    )

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