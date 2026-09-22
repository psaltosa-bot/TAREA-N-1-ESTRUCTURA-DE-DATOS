# EJERCICIO 13 — Mezclador de listas

class MezcladorListas:
    def mezclar(self, lista1, lista2):
        resultado = []
        limite = max(len(lista1), len(lista2))

        for i in range(limite):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def mezclar_varias(self, *listas):
        if not listas:
            return []

        resultado = list(listas[0])
        for lista in listas[1:]:
            resultado = self.mezclar(resultado, lista)

        return resultado


mezclador = MezcladorListas()
print(mezclador.mezclar([1, 3, 5], [2, 4, 6]))
print(mezclador.mezclar_varias([1, 2], ["a", "b"], [10, 20]))
