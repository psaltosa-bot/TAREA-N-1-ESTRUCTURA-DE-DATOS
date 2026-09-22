# EJERCICIO 20 — Analizador de patrones en textos

class AnalizadorTextos:
    def buscar_por_inicio(self, texto, patron):
        palabras = texto.split()
        return [
            palabra for palabra in palabras
            if palabra.startswith(patron)
        ]

    def agrupar_longitud(self, texto):
        resultado = {}
        for palabra in texto.split():
            longitud = len(palabra)
            if longitud not in resultado:
                resultado[longitud] = []
            resultado[longitud].append(palabra)
        return resultado

    def palabras_sin_repetir(self, texto):
        return set(texto.split())


analizador = AnalizadorTextos()
texto = "el gato está aquí y el gato juega"

print(analizador.buscar_por_inicio(texto, "g"))
print(analizador.agrupar_longitud(texto))
print(analizador.palabras_sin_repetir(texto))
