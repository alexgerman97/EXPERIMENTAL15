# Restaurante App - Semana 15

## Descripción

Restaurante App es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO) y la librería Tkinter para la interfaz gráfica.

La práctica de la Semana 15 corresponde a la evolución del proyecto de la Semana 14, incorporando un módulo de gestión de ventas, persistencia de información en archivos JSON y mejoras en la interfaz gráfica mediante la inclusión de logo e icono personalizados.

---

## Objetivo

Desarrollar una aplicación de escritorio que permita gestionar productos y ventas de un restaurante aplicando conceptos de:

- Programación Orientada a Objetos.
- Interfaces gráficas con Tkinter.
- Arquitectura por capas.
- Persistencia de datos mediante archivos JSON.
- Uso de eventos y callbacks mediante `command`.

---

## Estructura del Proyecto

```text
restaurante_app/
│
├── assets/
│   ├── logo.png
│   └── icono.ico
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── login_view.py
│   └── main_view.py
│
└── main.py
```

---

## Evolución respecto a la Semana 14

Durante la Semana 15 se añadieron las siguientes mejoras:

- Implementación de la clase `Venta`.
- Registro de ventas desde la interfaz gráfica.
- Visualización de ventas registradas.
- Persistencia de ventas en `ventas.json`.
- Inclusión de ComboBox para selección de usuarios y productos.
- Incorporación de logo e icono en la aplicación.
- Uso de callbacks mediante botones Tkinter.

---

## Funcionalidades Implementadas

### Inicio de Sesión

Permite validar usuarios registrados en el sistema.

### Gestión de Productos

El sistema permite:

- Registrar productos.
- Consultar productos.
- Actualizar productos.
- Eliminar productos.
- Mostrar listado de productos.

### Gestión de Usuarios

Permite visualizar los usuarios registrados.

### Gestión de Ventas

El sistema permite:

- Registrar ventas.
- Mostrar ventas registradas.
- Seleccionar usuarios mediante ComboBox.
- Seleccionar productos mediante ComboBox.

---

## Persistencia de Datos

La información se almacena en archivos JSON:

- productos.json
- usuarios.json
- ventas.json

Ejemplo de venta almacenada:

```json
{
    "usuario": "admin",
    "producto": "Hamburguesa",
    "fecha": "27/09/2026"
}
```

---

## Uso de command y callbacks

Los botones de la interfaz utilizan el parámetro `command` para ejecutar métodos cuando el usuario realiza una acción.

Ejemplo:

```python
tk.Button(
    self.frame_izquierdo,
    text="Registrar Venta",
    command=self.registrar_venta
)
```

Cuando el usuario presiona el botón, Tkinter ejecuta automáticamente el método asociado.

Este mecanismo permite implementar callbacks para responder a eventos de la interfaz gráfica.

---

## Tecnologías Utilizadas

- Python 3
- Tkinter
- JSON
- Pillow (PIL)
- Programación Orientada a Objetos (POO)

---

## Componentes Utilizados

### Contenedores

- Frame

### Componentes Gráficos

- Label
- Entry
- Button
- Text
- Combobox
- MessageBox

---

## Clases Implementadas

### Producto

Representa un producto del restaurante.

### Usuario

Representa un usuario del sistema.

### Venta

Representa una venta realizada en el restaurante.

### RestauranteServicio

Contiene la lógica de negocio para:

- Usuarios.
- Productos.
- Ventas.

### ArchivoServicio

Permite cargar y guardar información en archivos JSON.

### LoginView

Interfaz de inicio de sesión.

### MainView

Interfaz principal para la administración de productos y ventas.

---

## Cómo Ejecutar el Proyecto

1. Abrir Visual Studio Code.
2. Abrir la carpeta del proyecto.
3. Abrir una terminal.
4. Instalar Pillow:

```bash
pip install pillow
```

5. Ejecutar:

```bash
python restaurante_app/main.py
```

---

## Autor

Alex German Toaquiza Valiente

Universidad Estatal Amazónica

Programación Orientada a Objetos

Semana 15