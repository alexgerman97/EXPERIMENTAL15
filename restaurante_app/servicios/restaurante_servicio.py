from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(
        self,
        productos_data,
        usuarios_data,
        ventas_data=None
    ) -> None:
        self.archivo_servicio = ArchivoServicio()

        self.productos = []
        self.usuarios = []
        self.ventas = []

        self.cargar_productos(productos_data)
        self.cargar_usuarios(usuarios_data)
        self.cargar_ventas(ventas_data or [])

    # ==========================
    # CARGAR DATOS
    # ==========================

    def cargar_productos(self, datos) -> None:
        for producto in datos:
            try:
                self.productos.append(
                    Producto(
                        str(producto["codigo"]),
                        str(producto["nombre"]),
                        str(producto["categoria"]),
                        float(producto["precio"]),
                        int(producto["stock"])
                    )
                )
            except (KeyError, TypeError, ValueError):
                continue

    def cargar_usuarios(self, datos) -> None:
        for usuario in datos:
            try:
                self.usuarios.append(
                    Usuario(
                        str(usuario["usuario"]),
                        str(usuario["password"]),
                        str(usuario["nombre"])
                    )
                )
            except (KeyError, TypeError, ValueError):
                continue

    def cargar_ventas(self, datos) -> None:
        for venta in datos:
            try:
                self.ventas.append(
                    Venta(
                        str(venta["usuario"]),
                        str(venta["producto"]),
                        str(venta["fecha"]),
                        int(venta.get("cantidad", 1))
                    )
                )
            except (KeyError, TypeError, ValueError):
                continue

    # ==========================
    # LOGIN
    # ==========================

    def validar_login(self, usuario: str, contrasena: str) -> bool:
        for u in self.usuarios:
            if u.usuario == usuario and u.password == contrasena:
                return True
        return False

    # ==========================
    # PRODUCTOS
    # ==========================

    def registrar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ) -> bool:
        codigo = str(codigo).strip()
        nombre = str(nombre).strip()
        categoria = str(categoria).strip()

        if not codigo or not nombre or not categoria:
            raise ValueError("Todos los datos del producto son obligatorios.")

        try:
            precio = float(precio)
            stock = int(stock)
        except (TypeError, ValueError) as error:
            raise ValueError("Precio y stock deben ser numéricos.") from error

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        if self.consultar_producto(codigo):
            return False

        self.productos.append(
            Producto(codigo, nombre, categoria, precio, stock)
        )
        self._guardar_productos()
        return True

    def consultar_producto(self, codigo):
        codigo = str(codigo).strip()
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ) -> bool:
        producto = self.consultar_producto(codigo)

        if not producto:
            return False

        nombre = str(nombre).strip()
        categoria = str(categoria).strip()

        if not nombre or not categoria:
            raise ValueError("Nombre y categoría son obligatorios.")

        try:
            precio = float(precio)
            stock = int(stock)
        except (TypeError, ValueError) as error:
            raise ValueError("Precio y stock deben ser numéricos.") from error

        if precio < 0 or stock < 0:
            raise ValueError("Precio y stock no pueden ser negativos.")

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock

        self._guardar_productos()
        return True

    def eliminar_producto(self, codigo) -> bool:
        producto = self.consultar_producto(codigo)

        if not producto:
            return False

        self.productos.remove(producto)
        self._guardar_productos()
        return True

    def _guardar_productos(self) -> None:
        productos_json = [
            {
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "categoria": producto.categoria,
                "precio": producto.precio,
                "stock": producto.stock
            }
            for producto in self.productos
        ]
        self.archivo_servicio.guardar_productos(productos_json)

    # ==========================
    # VENTAS
    # ==========================

    def registrar_venta(
        self,
        usuario,
        producto,
        fecha,
        cantidad=1
    ) -> bool:
        usuario = str(usuario).strip()
        producto = str(producto).strip()
        fecha = str(fecha).strip()

        if not usuario or not producto or not fecha:
            raise ValueError("Complete todos los datos de la venta.")

        if not any(u.usuario == usuario for u in self.usuarios):
            raise ValueError("El usuario seleccionado no existe.")

        producto_obj = next(
            (p for p in self.productos if p.nombre == producto),
            None
        )

        if producto_obj is None:
            raise ValueError("El producto seleccionado no existe.")

        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError) as error:
            raise ValueError("La cantidad debe ser un número entero.") from error

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if producto_obj.stock < cantidad:
            raise ValueError("Stock insuficiente para realizar la venta.")

        nueva_venta = Venta(
            usuario,
            producto,
            fecha,
            cantidad
        )

        self.ventas.append(nueva_venta)
        producto_obj.stock -= cantidad

        self._guardar_productos()
        self._guardar_ventas()

        return True

    def _guardar_ventas(self) -> None:
        ventas_json = [
            {
                "usuario": venta.usuario,
                "producto": venta.producto,
                "fecha": venta.fecha,
                "cantidad": venta.cantidad
            }
            for venta in self.ventas
        ]
        self.archivo_servicio.guardar_ventas(ventas_json)

    def listar_ventas(self):
        return self.ventas

    def listar_ventas_usuario(self, usuario):
        return [
            venta
            for venta in self.ventas
            if venta.usuario == usuario
        ]

    # ==========================
    # LISTADOS
    # ==========================

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios
