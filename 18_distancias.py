# EJERCICIO 18 — Distancias entre puntos

import math

class Distancias:
    def __init__(self):
        self.distancias_calculadas = []

    def euclidiana(self, punto1, punto2):
        distancia = math.sqrt(
            (punto2[0] - punto1[0]) ** 2 +
            (punto2[1] - punto1[1]) ** 2
        )
        self.distancias_calculadas.append(distancia)
        return distancia

    def mas_cercano(self, origen, puntos):
        return min(
            puntos,
            key=lambda punto: self.euclidiana(origen, punto)
        )

    def distancias(self):
        return self.distancias_calculadas


distancias = Distancias()
origen = (0, 0)
puntos = [(3, 4), (1, 1), (5, 2)]
print(distancias.mas_cercano(origen, puntos))
print(distancias.distancias())
