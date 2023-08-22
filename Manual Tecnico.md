# Manual Técnico

## Clase Inventario

### Descripción

El archivo `Inventario.py` contiene la definición de la clase `Inventario` en Python. Esta clase se utiliza para representar elementos de inventario con información como nombre, cantidad, precio unitario y ubicación.

### Clase `Inventario`

La clase `Inventario` tiene los siguientes atributos y métodos:

#### Atributos

- `nombre`: Nombre del producto en el inventario.
- `cantidad`: Cantidad disponible del producto.
- `precioUnitario`: Precio unitario del producto.
- `ubicacion`: Ubicación física del producto en el almacén.
- `siguiente`: Referencia al siguiente elemento en la estructura (puede ser utilizado en estructuras de datos enlazadas).

#### Métodos

- `__init__(self, nombre, cantidad, precioUnitario, ubicacion)`: Constructor de la clase. Inicializa los atributos con los valores proporcionados.

### Uso

Aquí hay un ejemplo básico de cómo se podría usar la clase `Inventario`:

```python
from Inventario import Inventario

# Crear un objeto de inventario
producto1 = Inventario("Producto A", 10, 15.99, "Estante 1")

# Acceder a los atributos del objeto
print(producto1.nombre)
print(producto1.cantidad)
print(producto1.precioUnitario)
print(producto1.ubicacion)

```

## Clase Inventario_Dao

### Descripción

El archivo `Inventario_Dao.py` contiene la definición de la clase `Inventario_Dao` en Python. Esta clase proporciona métodos para gestionar un inventario utilizando la clase `Inventario` definida en el archivo `Inventario.py`.

### Clase `Inventario_Dao`

La clase `Inventario_Dao` tiene los siguientes atributos y métodos:

#### Atributos

- `inventarios`: Una lista que almacena objetos de la clase `Inventario` para representar los productos en el inventario.
- `contador_Productos`: Un contador para llevar un registro del número de productos en el inventario.

#### Métodos

- `__init__(self)`: Constructor de la clase. Inicializa la lista de inventarios y el contador de productos.
- `crear_producto(self, nombre, cantidad, precioUnitario, ubicacion)`: Crea un nuevo producto en el inventario si no hay un producto con el mismo nombre y ubicación. Retorna `True` si se creó con éxito, o `False` si no se pudo crear.
- `agregar_stock(self, nombre, cantidad, ubicacion)`: Agrega stock a un producto existente en el inventario. Retorna `True` si se agregó con éxito, o `False` si no se pudo agregar.
- `vender_stock(self, nombre, cantidad, ubicacion)`: Vende una cantidad específica de un producto existente en el inventario. Retorna `True` si se vendió con éxito, o `False` si no se pudo vender.
- `guardar_inventario_en_archivo(self, nombre_archivo)`: Guarda el inventario en un archivo de texto con un formato específico.
- `visualizar_stock(self)`: Muestra en la consola el stock actual en el inventario.

### Ejemplo de Uso

```python
from Inventario_Dao import Inventario_Dao

# Crear un objeto de Inventario_Dao
inventario_dao = Inventario_Dao()

# Crear productos
inventario_dao.crear_producto("Producto A", 10, 15.99, "Estante 1")
inventario_dao.crear_producto("Producto B", 20, 9.99, "Estante 2")

# Agregar stock
inventario_dao.agregar_stock("Producto A", 5, "Estante 1")

# Vender stock
inventario_dao.vender_stock("Producto B", 8, "Estante 2")

# Guardar inventario en un archivo
inventario_dao.guardar_inventario_en_archivo("informe_inventario.txt")

# Visualizar stock
inventario_dao.visualizar_stock()
```

## Clase Cargador

### Descripción

El archivo `Cargador.py` contiene la definición de la clase `cargador` en Python. Esta clase proporciona una interfaz gráfica desarrollada con la biblioteca tkinter para seleccionar archivos de inventario y cargarlos en la aplicación. La clase se comunica con la clase `Inventario_Dao` definida en el archivo `Inventario_Dao.py` para gestionar los datos del inventario.

### Clase `cargador`

La clase `cargador` tiene los siguientes atributos y métodos:

#### Atributos

- `root`: La ventana raíz de la interfaz gráfica.
- `selected_file_label`: Una etiqueta para mostrar "Archivo seleccionado:" en la interfaz.
- `file_path_label`: Una etiqueta que muestra la ruta del archivo seleccionado.
- `select_button`: Un botón para abrir el diálogo de selección de archivo.
- `manejador_Inventario`: Un objeto de la clase `Inventario_Dao` para interactuar con la gestión del inventario.

#### Métodos

- `__init__(self, root)`: Constructor de la clase. Inicializa los componentes de la interfaz gráfica.
- `select_file(self)`: Abre el diálogo de selección de archivo y muestra la ruta del archivo seleccionado en la etiqueta `file_path_label`.
- `select_file_Mov(self)`: Similar a `select_file`, pero para archivos de movimiento (*.mov).

#### Ejemplo de Uso

```python
import tkinter as tk
from tkinter import filedialog
from Inventario_Dao import Inventario_Dao

manejador_Inventario = Inventario_Dao()

class cargador:
    # ... (definición de la clase)

if __name__ == "__main__":
    root = tk.Tk()
    app = cargador(root)
    root.mainloop()

```


## Aplicación de Gestión de Inventario

### Descripción

El archivo `app.py` contiene el código de una aplicación de gestión de inventario en Python. La aplicación utiliza las clases definidas en `Inventario_Dao.py` y la interfaz gráfica proporcionada por la clase `cargador` definida en `cargador.py` para interactuar con los usuarios y gestionar el inventario.

### Funcionalidades

La aplicación ofrece las siguientes funcionalidades:

1. **Cargar inventario inicial**: Permite cargar un archivo que contiene instrucciones para crear productos en el inventario inicial.
2. **Cargar Instrucciones de Movimiento**: Permite cargar un archivo con instrucciones para agregar o vender stock en el inventario.
3. **Crear informe de Inventario**: Genera un informe en un archivo de texto que muestra el estado actual del inventario.
4. **Ver Inventario**: Muestra en la consola el stock actual en el inventario.
5. **Salir**: Cierra la aplicación.

### Uso

La aplicación se ejecuta en la consola. Los usuarios pueden elegir las opciones del menú ingresando el número correspondiente. La aplicación se comunica con las clases `Inventario_Dao` y `cargador` para realizar las operaciones necesarias.

```python
from Inventario_Dao import Inventario_Dao
import tkinter as tk
from cargador import cargador

manejador_Inventario = Inventario_Dao()

# Definición de funciones (registrar_Producto, agregar_Stock, ver_Inventario, crear_archivo, mostrar_menu)

if __name__ == "__main__":
    mostrar_menu()

```

# Estructura de Archivos

proyecto/

│   Inventario.py

│   Inventario_Dao.py

│   Cargador.py

│   app.py

│   main.py

│   README.md



© 2023 Julio