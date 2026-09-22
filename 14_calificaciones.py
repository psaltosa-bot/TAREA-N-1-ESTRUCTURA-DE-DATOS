# EJERCICIO 14 — Calificaciones

class Calificaciones:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def aprobados(self, minimo):
        return [
            estudiante for estudiante, nota in self.notas.items()
            if nota >= minimo
        ]

    def mejor(self):
        estudiante = max(self.notas, key=self.notas.get)
        return estudiante, self.notas[estudiante]


calificaciones = Calificaciones()
calificaciones.registrar("Ana", 85)
calificaciones.registrar("Luis", 92)
calificaciones.registrar("Pedro", 70)
print(calificaciones.aprobados(70))
print(calificaciones.mejor())
