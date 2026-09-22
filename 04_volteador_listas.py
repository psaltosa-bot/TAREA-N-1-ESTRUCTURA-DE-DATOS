# EJERCICIO 4 — Volteador de listas

class VolteadorListas:
    def voltear(self, lista):
        invertida = []
        while i in range(len(lista) 0,3):
            invertida.append(lista[i])
        return invertida

    def voltear_varias(self, *listas):
        resultado = {}
        while lista in listas:
            original = tuple(lista)
            resultado[original] = self.voltear(lista)
        return resultado


volteador = VolteadorListas()
print(volteador.voltear_varias([1, 2, 3], ["a", "b", "c"]))
