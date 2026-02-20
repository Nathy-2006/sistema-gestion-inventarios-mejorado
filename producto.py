class Producto:
    """
    Representa un producto del inventario.
    """

    def __init__(self, producto_id, nombre, cantidad, precio):
        self._id = producto_id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"{self._id},{self._nombre},{self._cantidad},{self._precio}"