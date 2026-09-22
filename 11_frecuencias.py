# EJERCICIO 11 — Frecuencias

class Frecuencias:
    def __init__(self):
        self.conteo = {}

    def registrar(self, elemento):
        if elemento in self.conteo:
            self.conteo[elemento] += 1
        else:
            self.conteo[elemento] = 1

    def mas_repetido(self):
        return max(self.conteo, key=self.conteo.get)

    def cantidad_de(self, elemento):
        return self.conteo.get(elemento, 0)


frecuencias = Frecuencias()
for elemento in ["a", "b", "a", "c", "a", "b"]:
    frecuencias.registrar(elemento)

print(frecuencias.conteo)
print(frecuencias.mas_repetido())
print(frecuencias.cantidad_de("b"))
