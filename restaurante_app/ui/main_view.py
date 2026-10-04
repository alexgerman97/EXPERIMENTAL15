import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class MainView:

    def __init__(
        self,
        root,
        restaurante_servicio,
        volver_login
    ) -> None:

        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.volver_login = volver_login

        self.frame = tk.Frame(root)
        self.frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self._cargar_logo()

        tk.Label(
            self.frame,
            text="PANEL PRINCIPAL DEL RESTAURANTE",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        # ==========================
        # CONTENEDORES
        # ==========================

        self.frame_izquierdo = tk.LabelFrame(
            self.frame,
            text="Gestión y ventas",
            padx=10,
            pady=5
        )
        self.frame_izquierdo.pack(
            side="left",
            fill="y",
            padx=10
        )

        self.frame_derecho = tk.LabelFrame(
            self.frame,
            text="Información del sistema",
            padx=5,
            pady=5
        )
        self.frame_derecho.pack(
            side="right",
            fill="both",
            expand=True,
            padx=10
        )

        self._crear_formulario_productos()
        self._crear_formulario_ventas()
        self._crear_botones()
        self._crear_area_resultados()
        self._actualizar_comboboxes()

    def _cargar_logo(self) -> None:
        ruta_logo = (
            Path(__file__).resolve().parent.parent
            / "assets"
            / "logo.png"
        )

        try:
            imagen = Image.open(ruta_logo)
            imagen.thumbnail((70, 70))
            self.logo = ImageTk.PhotoImage(imagen)

            tk.Label(
                self.frame,
                image=self.logo
            ).pack(pady=2)
        except (FileNotFoundError, OSError) as error:
            print(f"No se pudo cargar el logo: {error}")

    def _crear_formulario_productos(self) -> None:
        tk.Label(
            self.frame_izquierdo,
            text="PRODUCTOS",
            font=("Arial", 11, "bold")
        ).pack(pady=3)

        self.codigo_entry = self._crear_campo("Código")
        self.nombre_entry = self._crear_campo("Nombre")
        self.categoria_entry = self._crear_campo("Categoría")
        self.precio_entry = self._crear_campo("Precio")
        self.stock_entry = self._crear_campo("Stock")

    def _crear_campo(self, texto: str):
        tk.Label(
            self.frame_izquierdo,
            text=texto
        ).pack()

        entry = tk.Entry(
            self.frame_izquierdo,
            width=24
        )
        entry.pack(pady=1)
        return entry

    def _crear_formulario_ventas(self) -> None:
        tk.Label(
            self.frame_izquierdo,
            text="VENTAS",
            font=("Arial", 11, "bold")
        ).pack(pady=(6, 2))

        tk.Label(
            self.frame_izquierdo,
            text="Usuario"
        ).pack()

        self.usuario_combo = ttk.Combobox(
            self.frame_izquierdo,
            state="readonly",
            width=21
        )
        self.usuario_combo.pack(pady=1)

        tk.Label(
            self.frame_izquierdo,
            text="Producto"
        ).pack()

        self.producto_combo = ttk.Combobox(
            self.frame_izquierdo,
            state="readonly",
            width=21
        )
        self.producto_combo.pack(pady=1)

        tk.Label(
            self.frame_izquierdo,
            text="Cantidad"
        ).pack()

        self.cantidad_entry = tk.Entry(
            self.frame_izquierdo,
            width=24
        )
        self.cantidad_entry.insert(0, "1")
        self.cantidad_entry.pack(pady=1)

        tk.Label(
            self.frame_izquierdo,
            text="Fecha"
        ).pack()

        self.fecha_entry = tk.Entry(
            self.frame_izquierdo,
            width=24
        )
        self.fecha_entry.pack(pady=1)

    def _crear_botones(self) -> None:
        botones_frame = tk.Frame(
            self.frame_izquierdo
        )
        botones_frame.pack(
           pady=5
        )

        botones = [
            ("Registrar Producto", self.registrar_producto),
            ("Consultar Producto", self.consultar_producto),
            ("Actualizar Producto", self.actualizar_producto),
            ("Eliminar Producto", self.eliminar_producto),
            ("Mostrar Productos", self.mostrar_productos),
            ("Mostrar Usuarios", self.mostrar_usuarios),
            ("Registrar Venta", self.registrar_venta),
            ("Mostrar Ventas", self.mostrar_ventas),
            ("Ventas por Usuario", self.mostrar_ventas_usuario),
            ("Cerrar Sesión", self.cerrar_sesion)
        ]

        for indice, (texto, comando) in enumerate(botones):
            fila = indice // 2
            columna = indice % 2

            tk.Button(
                botones_frame,
                text=texto,
                command=comando,
                width=18
            ).grid(
                row=fila,
                column=columna,
                padx=2,
                pady=2
            )

    def _crear_area_resultados(self) -> None:
        self.texto = tk.Text(
            self.frame_derecho,
            width=65,
            height=25,
            wrap="word"
        )
        self.texto.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

    def _actualizar_comboboxes(self) -> None:
        self.usuario_combo["values"] = [
            usuario.usuario
            for usuario in self.restaurante_servicio.listar_usuarios()
        ]

        self.producto_combo["values"] = [
            producto.nombre
            for producto in self.restaurante_servicio.listar_productos()
        ]

    # ==========================
    # CRUD PRODUCTOS
    # ==========================

    def registrar_producto(self) -> None:
        try:
            resultado = self.restaurante_servicio.registrar_producto(
                self.codigo_entry.get(),
                self.nombre_entry.get(),
                self.categoria_entry.get(),
                self.precio_entry.get(),
                self.stock_entry.get()
            )

            if resultado:
                messagebox.showinfo(
                    "Correcto",
                    "Producto registrado y guardado correctamente."
                )
                self._actualizar_comboboxes()
                self.mostrar_productos()
            else:
                messagebox.showerror(
                    "Error",
                    "El código del producto ya existe."
                )

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def consultar_producto(self) -> None:
        codigo = self.codigo_entry.get().strip()
        producto = self.restaurante_servicio.consultar_producto(codigo)

        if not producto:
            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )
            return

        for entry, valor in [
            (self.nombre_entry, producto.nombre),
            (self.categoria_entry, producto.categoria),
            (self.precio_entry, producto.precio),
            (self.stock_entry, producto.stock)
        ]:
            entry.delete(0, tk.END)
            entry.insert(0, valor)

        messagebox.showinfo(
            "Consulta",
            "Producto cargado en el formulario."
        )

    def actualizar_producto(self) -> None:
        try:
            resultado = self.restaurante_servicio.actualizar_producto(
                self.codigo_entry.get(),
                self.nombre_entry.get(),
                self.categoria_entry.get(),
                self.precio_entry.get(),
                self.stock_entry.get()
            )

            if resultado:
                messagebox.showinfo(
                    "Correcto",
                    "Producto actualizado y guardado correctamente."
                )
                self._actualizar_comboboxes()
                self.mostrar_productos()
            else:
                messagebox.showerror(
                    "Error",
                    "Producto no encontrado."
                )

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def eliminar_producto(self) -> None:
        codigo = self.codigo_entry.get().strip()

        if not codigo:
            messagebox.showerror(
                "Error",
                "Ingrese el código del producto."
            )
            return

        resultado = self.restaurante_servicio.eliminar_producto(codigo)

        if resultado:
            messagebox.showinfo(
                "Correcto",
                "Producto eliminado y cambios guardados."
            )
            self._actualizar_comboboxes()
            self.mostrar_productos()
        else:
            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )

    # ==========================
    # CONSULTAS
    # ==========================

    def mostrar_productos(self) -> None:
        self.texto.delete("1.0", tk.END)
        productos = self.restaurante_servicio.listar_productos()

        self.texto.insert(
            tk.END,
            "=== PRODUCTOS REGISTRADOS ===\n\n"
        )

        for producto in productos:
            self.texto.insert(
                tk.END,
                f"Código: {producto.codigo}\n"
                f"Nombre: {producto.nombre}\n"
                f"Categoría: {producto.categoria}\n"
                f"Precio: ${producto.precio:.2f}\n"
                f"Stock: {producto.stock}\n\n"
            )

    def mostrar_usuarios(self) -> None:
        self.texto.delete("1.0", tk.END)
        usuarios = self.restaurante_servicio.listar_usuarios()

        self.texto.insert(
            tk.END,
            "=== USUARIOS REGISTRADOS ===\n\n"
        )

        for usuario in usuarios:
            self.texto.insert(
                tk.END,
                f"Usuario: {usuario.usuario}\n"
                f"Nombre: {usuario.nombre}\n\n"
            )

    # ==========================
    # VENTAS
    # ==========================

    def registrar_venta(self) -> None:
        try:
            self.restaurante_servicio.registrar_venta(
                self.usuario_combo.get(),
                self.producto_combo.get(),
                self.fecha_entry.get(),
                self.cantidad_entry.get()
            )

            messagebox.showinfo(
                "Correcto",
                "Venta registrada correctamente.\n"
                "La venta y el nuevo stock fueron guardados."
            )

            self._actualizar_comboboxes()
            self.mostrar_ventas()

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def mostrar_ventas(self) -> None:
        self.texto.delete("1.0", tk.END)
        ventas = self.restaurante_servicio.listar_ventas()

        self.texto.insert(
            tk.END,
            "=== VENTAS REGISTRADAS ===\n\n"
        )

        if not ventas:
            self.texto.insert(tk.END, "No existen ventas registradas.\n")
            return

        for venta in ventas:
            self.texto.insert(
                tk.END,
                f"Usuario: {venta.usuario}\n"
                f"Producto: {venta.producto}\n"
                f"Cantidad: {venta.cantidad}\n"
                f"Fecha: {venta.fecha}\n\n"
            )

    def mostrar_ventas_usuario(self) -> None:
        usuario = self.usuario_combo.get()

        if not usuario:
            messagebox.showerror(
                "Error",
                "Seleccione un usuario."
            )
            return

        ventas = self.restaurante_servicio.listar_ventas_usuario(usuario)

        self.texto.delete("1.0", tk.END)
        self.texto.insert(
            tk.END,
            f"=== VENTAS DEL USUARIO: {usuario} ===\n\n"
        )

        if not ventas:
            self.texto.insert(
                tk.END,
                "El usuario no tiene ventas registradas.\n"
            )
            return

        for venta in ventas:
            self.texto.insert(
                tk.END,
                f"Producto: {venta.producto}\n"
                f"Cantidad: {venta.cantidad}\n"
                f"Fecha: {venta.fecha}\n\n"
            )

    # ==========================
    # SESIÓN
    # ==========================

    def cerrar_sesion(self) -> None:
        respuesta = messagebox.askyesno(
            "Cerrar sesión",
            "¿Desea cerrar sesión?"
        )

        if respuesta:
            self.frame.destroy()
            self.volver_login()
