# EJERCICIO 15 — Buscador de divisores

class BuscadorDivisores:
    def divisores(self, numero):
        resultado = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                resultado.append(i)
        return tuple(resultado)

    def es_perfecto(self, numero):
        divisores_propios = [
            divisor for divisor in self.divisores(numero)
            if divisor != numero
        ]
        return sum(divisores_propios) == numero

    def divisores_de_varios(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.divisores(numero)
        return resultado


buscador = BuscadorDivisores()
print(buscador.divisores(12))
print(buscador.es_perfecto(28))
print(buscador.divisores_de_varios(6, 10, 12))
