# EJERCICIO 3 — Lista de precios

class ListaPrecios:
    def __init__(self):
        self.productos = {}

    def registrar(self, nombre, precio):
        self.productos[nombre] = precio

    def valor_total(self):
        return sum(self.productos.values())

    def filtrar_por_precio(self, minimo, maximo):
        return {
            nombre: precio
            for nombre, precio in self.productos.items()
            if minimo <= precio <= maximo
        }


lista = ListaPrecios()
lista.registrar("Cuaderno", 3.50)
lista.registrar("Mochila", 25)
lista.registrar("Lapicero", 1.50)
print(lista.valor_total())
print(lista.filtrar_por_precio(2, 20))
