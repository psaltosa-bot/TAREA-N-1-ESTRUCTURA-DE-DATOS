# EJERCICIO 19 — Almacén de productos

class Almacen:
    def __init__(self):
        self.stock = {}

    def ingresar(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def retirar(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def bajo_minimo(self, minimo):
        return [
            producto for producto, cantidad in self.stock.items()
            if cantidad < minimo
        ]


almacen = Almacen()
almacen.ingresar("Cuadernos", 20)
almacen.ingresar("Lapices", 8)
print(almacen.retirar("Cuadernos", 5))
print(almacen.retirar("Lapices", 10))
print(almacen.stock)
print(almacen.bajo_minimo(10))
