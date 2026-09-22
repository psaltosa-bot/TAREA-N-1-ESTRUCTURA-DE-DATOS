# EJERCICIO 7 — Directorio de edades

class DirectorioEdades:
    def __init__(self):
        self.personas = {}

    def agregar(self, nombre, edad):
        self.personas[nombre] = edad

    def mayores_que(self, edad_minima):
        return [
            nombre for nombre, edad in self.personas.items()
            if edad >= edad_minima
        ]

    def promedio_edades(self):
        return sum(self.personas.values()) / len(self.personas)


directorio = DirectorioEdades()
directorio.agregar("Ana", 17)
directorio.agregar("Luis", 25)
directorio.agregar("Pedro", 31)
print(directorio.mayores_que(18))
print(directorio.promedio_edades())
