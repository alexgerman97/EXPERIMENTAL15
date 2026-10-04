# Restaurante App - Semana 15

## Descripción

Restaurante App es una aplicación de escritorio desarrollada en Python con Programación Orientada a Objetos (POO) y Tkinter. La Semana 15 evoluciona la versión gráfica anterior incorporando la gestión de ventas, persistencia de ventas en `ventas.json`, actualización del stock y callbacks mediante `command=`.

## Objetivo de la Semana 15

Integrar una operación de venta dentro de la aplicación gráfica manteniendo la separación entre interfaz, modelos, servicios y archivos JSON.

## Evolución respecto a la Semana 14

Se incorporaron:

- Clase `Venta`.
- Registro y consulta de ventas desde la interfaz.
- Consulta de ventas por usuario.
- Persistencia de `ventas.json`.
- Actualización y persistencia del stock después de una venta.
- Validación de usuario, producto, cantidad y stock.
- Combobox para seleccionar usuarios y productos.
- Campo de cantidad y fecha para la venta.
- Logo e icono del restaurante.
- Callbacks de los botones mediante `command=`.

## Estructura del proyecto

```text
restaurante_app/
├── assets/
│   ├── logo.png
│   └── icono.ico
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Responsabilidad de los módulos

- `modelos/`: representa los objetos `Producto`, `Usuario` y `Venta`.
- `servicios/archivo_servicio.py`: centraliza la lectura y escritura de los archivos JSON.
- `servicios/restaurante_servicio.py`: contiene las operaciones y validaciones del restaurante.
- `ui/login_view.py`: gestiona el inicio de sesión.
- `ui/main_view.py`: presenta formularios, botones, consultas y gestión de ventas.
- `main.py`: crea la ventana principal, carga los datos y conecta las vistas con el servicio.
- `datos/`: contiene los archivos JSON persistentes.
- `assets/`: contiene los recursos gráficos utilizados por la interfaz.

## Gestión de productos

Desde la interfaz se pueden:

- Registrar productos.
- Consultar productos.
- Actualizar productos.
- Eliminar productos.
- Mostrar productos.

Los cambios de productos se guardan en `productos.json`.

## Gestión de ventas

Para registrar una venta se seleccionan:

1. Usuario.
2. Producto.
3. Cantidad.
4. Fecha.

`RestauranteServicio` valida los datos, comprueba el stock disponible, crea un objeto `Venta`, disminuye el stock y guarda los cambios en `ventas.json` y `productos.json`.

También se puede consultar el listado general de ventas y las ventas de un usuario seleccionado.

## Persistencia

La aplicación utiliza:

- `productos.json` para productos y stock.
- `usuarios.json` para usuarios.
- `ventas.json` para ventas.

Al iniciar la aplicación, `main.py` carga los tres archivos mediante `ArchivoServicio` y `RestauranteServicio` reconstruye los objetos utilizados por el sistema.

## Uso de `command=` y callbacks

Los botones de Tkinter utilizan `command=` para asociar una acción con un método de `MainView` o `LoginView`.

Ejemplo:

```python
tk.Button(
    self.frame_izquierdo,
    text="Registrar Venta",
    command=self.registrar_venta
)
```

Al presionar el botón, Tkinter ejecuta el método `registrar_venta`, que solicita la operación a `RestauranteServicio`.

## Recursos visuales

- `assets/logo.png`: se muestra en la interfaz principal.
- `assets/icono.ico`: se utiliza como icono de la ventana.

La aplicación utiliza Pillow para cargar el recurso gráfico `logo.png`.

## Cómo ejecutar

1. Abrir la carpeta `EXPERIMENTAL15` en Visual Studio Code.
2. Abrir una terminal en la carpeta raíz del repositorio.
3. Instalar Pillow si todavía no está instalado:

```bash
pip install pillow
```

4. Ejecutar:

```bash
python restaurante_app/main.py
```

## Pruebas realizadas

Se debe comprobar el siguiente flujo antes de entregar:

1. Ejecutar `main.py`.
2. Iniciar sesión con un usuario registrado.
3. Consultar usuarios y productos.
4. Registrar, consultar, actualizar y eliminar un producto.
5. Confirmar que los cambios se guarden en `productos.json`.
6. Registrar una venta con stock disponible.
7. Confirmar que `ventas.json` registre la venta.
8. Confirmar que el stock del producto disminuya.
9. Consultar las ventas registradas.
10. Cerrar y volver a ejecutar la aplicación.
11. Confirmar que productos y ventas se recuperen desde los archivos JSON.
12. Intentar vender una cantidad mayor al stock y comprobar que la operación sea rechazada.

## Autor

Alex German Toaquiza Valiente  
Universidad Estatal Amazónica  
Programación Orientada a Objetos - Semana 15
