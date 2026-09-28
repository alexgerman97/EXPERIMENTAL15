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
    ):
        self.archivo_servicio = ArchivoServicio()

        self.productos = []
        self.usuarios = []
        self.ventas = []

        self.cargar_productos(productos_data)
        self.cargar_usuarios(usuarios_data)

        if ventas_data:
            self.cargar_ventas(ventas_data)

    # ==========================
    # CARGAR DATOS
    # ==========================

    def cargar_productos(
        self,
        datos
    ):

        for producto in datos:

            self.productos.append(
                Producto(
                    producto["codigo"],
                    producto["nombre"],
                    producto["categoria"],
                    producto["precio"],
                    producto["stock"]
                )
            )

    def cargar_usuarios(
        self,
        datos
    ):

        for usuario in datos:

            self.usuarios.append(
                Usuario(
                    usuario["usuario"],
                    usuario["password"],
                    usuario["nombre"]
                )
            )

    def cargar_ventas(
        self,
        datos
    ):

        for venta in datos:

            self.ventas.append(
                Venta(
                    venta["usuario"],
                    venta["producto"],
                    venta["fecha"]
                )
            )

    # ==========================
    # LOGIN
    # ==========================

    def validar_login(
        self,
        usuario,
        contrasena
    ):

        for u in self.usuarios:

            if (
                u.usuario == usuario
                and
                u.password == contrasena
            ):

                return True

        return False

    # ==========================
    # CRUD PRODUCTOS
    # ==========================

    def registrar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ):

        for producto in self.productos:

            if producto.codigo == codigo:
                return False

        nuevo_producto = Producto(
            codigo,
            nombre,
            categoria,
            float(precio),
            int(stock)
        )

        self.productos.append(
            nuevo_producto
        )

        return True

    def consultar_producto(
        self,
        codigo
    ):

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
    ):

        producto = self.consultar_producto(
            codigo
        )

        if producto:

            producto.nombre = nombre
            producto.categoria = categoria
            producto.precio = float(precio)
            producto.stock = int(stock)

            return True

        return False

    def eliminar_producto(
        self,
        codigo
    ):

        producto = self.consultar_producto(
            codigo
        )

        if producto:

            self.productos.remove(
                producto
            )

            return True

        return False

    # ==========================
    # VENTAS
    # ==========================

    def registrar_venta(
        self,
        usuario,
        producto,
        fecha
    ):

        nueva_venta = Venta(
            usuario,
            producto,
            fecha
        )

        self.ventas.append(
            nueva_venta
        )

        ventas_json =[]

        for venta in self.ventas:

            ventas_json.append(
                {
                    "usuario": venta.usuario,
                    "producto": venta.producto,
                    "fecha": venta.fecha
                }    
            )

        self.archivo_servicio.guardar_ventas(
            ventas_json
        ) 

        return True


    def listar_ventas(self):

               return self.ventas
    # ==========================
    # LISTADOS
    # ==========================

    def listar_productos(self):

        return self.productos

    def listar_usuarios(self):

        return self.usuarios