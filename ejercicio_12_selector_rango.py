class SelectorRango:
    def __init__(self):
        self.rangos_creados = []

    def crear_rango(self, inicio, fin):
        rango = tuple(range(inicio, fin + 1))
        self.rangos_creados.append(rango)
        return rango

    def elementos_en_multiples_rangos(self, *rangos):
        combinados = set()
        for inicio, fin in rangos:
            rango = self.crear_rango(inicio, fin)
            combinados.update(rango)
        return sorted(combinados)


sr = SelectorRango()
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))
