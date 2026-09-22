# EJERCICIO 5 — Clasificador de números

class ClasificadorNumeros:
    def es_par(self, numero):
        return numero % 2 == 0

    def clasificar(self, *numeros):
        resultado = {"pares": [], "impares": []}
        for numero in numeros:
            if self.es_par(numero):
                resultado["pares"].append(numero)
            else:
                resultado["impares"].append(numero)
        return resultado

    def cantidades(self, *numeros):
        resultado = self.clasificar(*numeros)
        return len(resultado["pares"]), len(resultado["impares"])


clasificador = ClasificadorNumeros()
print(clasificador.clasificar(1, 2, 3, 4, 5, 6))
print(clasificador.cantidades(1, 2, 3, 4, 5, 6))
