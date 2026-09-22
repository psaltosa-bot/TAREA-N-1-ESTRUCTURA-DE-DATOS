# EJERCICIO 6 — Control de temperaturas

class ControlClima:
    def __init__(self):
        self.temperaturas = []

    def registrar(self, temperatura):
        self.temperaturas.append(temperatura)

    def menor(self):
        return min(self.temperaturas)

    def mayor(self):
        return max(self.temperaturas)

    def media(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_varias(self, *temperaturas):
        for temperatura in temperaturas:
            self.registrar(temperatura)


clima = ControlClima()
clima.registrar_varias(22, 25, 19, 27, 24)
print(clima.temperaturas)
print(clima.menor())
print(clima.mayor())
print(clima.media())
