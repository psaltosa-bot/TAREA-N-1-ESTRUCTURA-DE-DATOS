# EJERCICIO 1 — Control de puntajes

class ControlPuntajes:
    def __init__(self):
        self.puntajes = []

    def es_valido(self, puntaje):
        return 0 <= puntaje <= 100

    def registrar_varios(self, *puntajes):
        for puntaje in puntajes:
            if self.es_valido(puntaje):
                self.puntajes.append(puntaje)
        return self.puntajes

    def promedio(self):
        if not self.puntajes:
            return 0
        return sum(self.puntajes) / len(self.puntajes)


control = ControlPuntajes()
print(control.registrar_varios(80, 95, 110, -5, 70))
print(control.promedio())
