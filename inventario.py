from producto import Producto


class Inventario:
    """
    Gestiona productos y su almacenamiento en archivo.
    """

    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # =========================
    # Cargar inventario
    # =========================
    def cargar_desde_archivo(self):
        """
        Lee el archivo y reconstruye el inventario.
        """
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        p = Producto(
                            int(datos[0]),
                            datos[1],
                            int(datos[2]),
                            float(datos[3])
                        )
                        self.productos.append(p)

        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()

        except PermissionError:
            print("Sin permisos para leer el archivo.")

        except Exception as e:
            print("Error leyendo archivo:", e)

    # =========================
    # Guardar inventario
    # =========================
    def guardar_archivo(self):
        """
        Escribe todos los productos al archivo.
        """
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(str(p) + "\n")

            print(" Inventario guardado correctamente.")

        except PermissionError:
            print(" No hay permisos para escribir el archivo.")

        except Exception as e:
            print("Error al guardar:", e)

    # =========================
    # Operaciones
    # =========================
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" ID duplicado.")
                return

        self.productos.append(producto)
        self.guardar_archivo()
        print(" Producto agregado y guardado.")

    def eliminar_producto(self, producto_id):
        for p in self.productos:
            if p.get_id() == producto_id:
                self.productos.remove(p)
                self.guardar_archivo()
                print("🗑 Producto eliminado.")
                return

        print(" Producto no encontrado.")

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == producto_id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                self.guardar_archivo()
                print("✏ Producto actualizado.")
                return

        print(" Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]

        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print(" No se encontraron productos.")

    def mostrar_todos(self):
        if not self.productos:
            print(" Inventario vacío.")
        else:
            for p in self.productos:
                print(p)