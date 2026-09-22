class CalculadorDistancia:
    def __init__(self):
        self.distancias_calculadas = []

    def distancia_euclidiana(self, p1, p2):
        distancia = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
        self.distancias_calculadas.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        mas_cercano = None
        menor_distancia = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)
            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                mas_cercano = punto
        return mas_cercano


cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))
print(cd.punto_mas_cercano((0, 0), (3, 4), (1, 1), (10, 10)))
