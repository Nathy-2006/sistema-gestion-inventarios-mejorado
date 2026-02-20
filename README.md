Descripción

Aplicación en Python que implementa un sistema de gestión de inventarios utilizando programación orientada a objetos. 
El sistema permite administrar productos mediante operaciones CRUD y garantiza persistencia de datos usando archivos de texto,
junto con manejo de excepciones para asegurar robustez ante errores de lectura y escritura.

Funcionalidades

Añadir productos con validación de ID.
Eliminar productos del inventario.
Actualizar cantidad y precio.
Búsqueda por nombre.
Visualización completa del inventario.
Persistencia automática en archivo.
Carga del inventario al iniciar el programa.
Manejo de errores de entrada y archivos.

Arquitectura del Proyecto

producto.py → Define la entidad Producto.

inventario.py → Gestiona lógica del inventario, archivos y excepciones.

sistema_inventario.py → Interfaz de usuario en consola.

inventario.txt → Almacenamiento persistente.

