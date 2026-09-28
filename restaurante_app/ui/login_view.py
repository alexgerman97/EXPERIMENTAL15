import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(
        self,
        root,
        restaurante_servicio,
        mostrar_main
    ) -> None:

        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_main = mostrar_main

        self.frame = tk.Frame(root)
        self.frame.pack(pady=50)

        tk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        tk.Label(
            self.frame,
            text="Usuario"
        ).pack()

        self.usuario_entry = tk.Entry(
            self.frame
        )
        self.usuario_entry.pack()

        tk.Label(
            self.frame,
            text="Contraseña"
        ).pack()

        self.password_entry = tk.Entry(
            self.frame,
            show="*"
        )
        self.password_entry.pack()

        tk.Button(
            self.frame,
            text="Ingresar",
            command=self.login
        ).pack(pady=10)

    def login(self) -> None:

        usuario = self.usuario_entry.get().strip()

        contrasena = self.password_entry.get().strip()

        if (
            usuario == ""
            or
            contrasena == ""
        ):

            messagebox.showerror(
                "Error",
                "Complete todos los campos"
            )

            return

        if self.restaurante_servicio.validar_login(
            usuario,
            contrasena
        ):

            messagebox.showinfo(
                "Acceso correcto",
                f"Bienvenido {usuario}"
            )

            self.frame.destroy()

            self.mostrar_main()

        else:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos"
            )