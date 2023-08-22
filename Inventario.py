class Inventario:
    def __init__(self,nombre,cantidad,precioUnitario,ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario
        self.ubicacion = ubicacion
        self.siguiente = None