class DivisorFinder:
    def __init__(self):
        self.historial = {}

    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = sum(divisores) - numero
        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        self.historial.update(resultado)
        return resultado


df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(28))
print(df.encontrar_multiples_divisores(6, 12))
