import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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
            padx=20,
            pady=20
        )

        try:

            imagen = Image.open(
                "restaurante_app/assets/logo.png"
            )

            imagen = imagen.resize(
                (70, 70)
            )

            self.logo = ImageTk.PhotoImage(
                imagen
            )

            tk.Label(
                self.frame,
                image=self.logo
            ).pack(pady=2)

        except Exception as e:

            print("ERROR LOGO:", e)

        tk.Label(
            self.frame,
            text="PANEL PRINCIPAL DEL RESTAURANTE",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        # ==========================
        # CONTENEDORES
        # ==========================

        self.frame_izquierdo = tk.Frame(
            self.frame,
            bd=2,
            relief="groove"
        )

        self.frame_izquierdo.pack(
            side="left",
            fill="y",
            padx=10
        )

        self.frame_derecho = tk.Frame(
            self.frame,
            bd=2,
            relief="groove"
        )

        self.frame_derecho.pack(
            side="right",
            fill="both",
            expand=True,
            padx=10
        )

        # ==========================
        # FORMULARIO PRODUCTOS
        # ==========================

        tk.Label(
            self.frame_izquierdo,
            text="GESTIÓN DE PRODUCTOS",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        tk.Label(
            self.frame_izquierdo,
            text="Código"
        ).pack()

        self.codigo_entry = tk.Entry(
            self.frame_izquierdo
        )

        self.codigo_entry.pack()

        tk.Label(
            self.frame_izquierdo,
            text="Nombre"
        ).pack()

        self.nombre_entry = tk.Entry(
            self.frame_izquierdo
        )

        self.nombre_entry.pack()

        tk.Label(
            self.frame_izquierdo,
            text="Categoría"
        ).pack()

        self.categoria_entry = tk.Entry(
            self.frame_izquierdo
        )

        self.categoria_entry.pack()

        tk.Label(
            self.frame_izquierdo,
            text="Precio"
        ).pack()

        self.precio_entry = tk.Entry(
            self.frame_izquierdo
        )

        self.precio_entry.pack()

        tk.Label(
            self.frame_izquierdo,
            text="Stock"
        ).pack()

        self.stock_entry = tk.Entry(
            self.frame_izquierdo
        )

        self.stock_entry.pack()

        # ==========================
        # VENTAS
        # ==========================

        tk.Label(
            self.frame_izquierdo,
            text="Usuario Venta"
        ).pack()

        self.usuario_combo = ttk.Combobox(
            self.frame_izquierdo,
            state="readonly"
        )

        self.usuario_combo.pack()

        self.usuario_combo["values"] = [
            usuario.usuario
            for usuario in self.restaurante_servicio.listar_usuarios()
        ]

        tk.Label(
            self.frame_izquierdo,
            text="Producto Venta"
        ).pack()

        self.producto_combo = ttk.Combobox(
            self.frame_izquierdo,
            state="readonly"
       )

        self.producto_combo.pack()

        self.producto_combo["values"] = [
            producto.nombre
            for producto in self.restaurante_servicio.listar_productos()
        ]

        tk.Label(
            self.frame_izquierdo,
            text="Fecha"
        ).pack()

        self.fecha_entry = tk.Entry(
            self.frame_izquierdo
        )

        self.fecha_entry.pack()

        # ==========================
        # BOTONES CRUD
        # ==========================

        tk.Button(
            self.frame_izquierdo,
            text="Registrar Producto",
            command=self.registrar_producto
        ).pack(pady=2)

        tk.Button(
            self.frame_izquierdo,
            text="Consultar Producto",
            command=self.consultar_producto
        ).pack(pady=2)

        tk.Button(
            self.frame_izquierdo,
            text="Actualizar Producto",
            command=self.actualizar_producto
        ).pack(pady=2)

        tk.Button(
            self.frame_izquierdo,
            text="Eliminar Producto",
            command=self.eliminar_producto
        ).pack(pady=2)

        tk.Button(
            self.frame_izquierdo,
            text="Mostrar Productos",
            command=self.mostrar_productos
        ).pack(pady=2)

        tk.Button(
            self.frame_izquierdo,
            text="Mostrar Usuarios",
            command=self.mostrar_usuarios
        ).pack(pady=2)

        tk.Button(
            self.frame_izquierdo,
            text="Registrar Venta",
            command=self.registrar_venta
        ).pack(pady=2)

        tk.Button(
            self.frame_izquierdo,
            text="Mostrar Ventas",
            command=self.mostrar_ventas
        ).pack(pady=2)

        tk.Button(
            self.frame_izquierdo,
            text="Cerrar Sesión",
            command=self.cerrar_sesion
        ).pack(pady=5)

        # ==========================
        # ÁREA DE RESULTADOS
        # ==========================

        self.texto = tk.Text(
            self.frame_derecho,
            width=70,
            height=25
        )

        self.texto.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    # ==========================
    # CRUD PRODUCTOS
    # ==========================

    def registrar_producto(self):

        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        categoria = self.categoria_entry.get()
        precio = self.precio_entry.get()
        stock = self.stock_entry.get()

        if (
            codigo == "" or
            nombre == "" or
            categoria == "" or
            precio == "" or
            stock == ""
        ):

            messagebox.showerror(
                "Error",
                "Complete todos los campos"
            )

            return

        resultado = (
            self.restaurante_servicio
            .registrar_producto(
                codigo,
                nombre,
                categoria,
                precio,
                stock
            )
        )

        if resultado:

            messagebox.showinfo(
                "Correcto",
                "Producto registrado"
            )

        else:

            messagebox.showerror(
                "Error",
                "El código ya existe"
            )

    def consultar_producto(self):

        codigo = self.codigo_entry.get()

        producto = (
            self.restaurante_servicio
            .consultar_producto(
                codigo
            )
        )

        if producto:

            self.nombre_entry.delete(0, tk.END)
            self.categoria_entry.delete(0, tk.END)
            self.precio_entry.delete(0, tk.END)
            self.stock_entry.delete(0, tk.END)

            self.nombre_entry.insert(
                0,
                producto.nombre
            )

            self.categoria_entry.insert(
                0,
                producto.categoria
            )

            self.precio_entry.insert(
                0,
                producto.precio
            )

            self.stock_entry.insert(
                0,
                producto.stock
            )

        else:

            messagebox.showerror(
                "Error",
                "Producto no encontrado"
            )

    def actualizar_producto(self):

        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        categoria = self.categoria_entry.get()
        precio = self.precio_entry.get()
        stock = self.stock_entry.get()

        resultado = (
            self.restaurante_servicio
            .actualizar_producto(
                codigo,
                nombre,
                categoria,
                precio,
                stock
            )
        )

        if resultado:

            messagebox.showinfo(
                "Correcto",
                "Producto actualizado"
            )

        else:

            messagebox.showerror(
                "Error",
                "Producto no encontrado"
            )

    def eliminar_producto(self):

        codigo = self.codigo_entry.get()

        resultado = (
            self.restaurante_servicio
            .eliminar_producto(
                codigo
            )
        )

        if resultado:

            messagebox.showinfo(
                "Correcto",
                "Producto eliminado"
            )

        else:

            messagebox.showerror(
                "Error",
                "Producto no encontrado"
            )

    # ==========================
    # CONSULTAS
    # ==========================

    def mostrar_productos(self) -> None:

        self.texto.delete(
            "1.0",
            tk.END
        )

        productos = (
            self.restaurante_servicio
            .listar_productos()
        )

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
                f"Precio: ${producto.precio}\n"
                f"Stock: {producto.stock}\n\n"
            )

    def mostrar_usuarios(self) -> None:

        self.texto.delete(
            "1.0",
            tk.END
        )

        usuarios = (
            self.restaurante_servicio
            .listar_usuarios()
        )

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

    def registrar_venta(self):

        usuario = self.usuario_combo.get()
        producto = self.producto_combo.get()
        fecha = self.fecha_entry.get()

        if (
            usuario == ""
            or producto == ""
            or fecha == ""
        ):

            messagebox.showerror(
                "Error",
                "Complete todos los datos"
            )

            return

        self.restaurante_servicio.registrar_venta(
            usuario,
            producto,
            fecha
        )

        messagebox.showinfo(
            "Correcto",
            "Venta registrada"
        )

    def mostrar_ventas(self):

        self.texto.delete(
            "1.0",
            tk.END
        )

        ventas = (
            self.restaurante_servicio
            .listar_ventas()
        )

        self.texto.insert(
            tk.END,
            "=== VENTAS REGISTRADAS ===\n\n"
        )

        for venta in ventas:

            self.texto.insert(
                tk.END,
                f"Usuario: {venta.usuario}\n"
                f"Producto: {venta.producto}\n"
                f"Fecha: {venta.fecha}\n\n"
            )            

    def cerrar_sesion(self) -> None:

        respuesta = messagebox.askyesno(
            "Cerrar sesión",
            "¿Desea cerrar sesión?"
        )

        if respuesta:

            self.frame.destroy()

            self.volver_login()