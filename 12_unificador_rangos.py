# EJERCICIO 12 — Unificador de rangos

class UnificadorRangos:
    def rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def combinar(self, *rangos):
        valores = set()
        for inicio, fin in rangos:
            valores.update(self.rango(inicio, fin))
        return list(valores)


unificador = UnificadorRangos()
print(unificador.rango(1, 5))
print(unificador.combinar((1, 5), (4, 8), (10, 12)))
