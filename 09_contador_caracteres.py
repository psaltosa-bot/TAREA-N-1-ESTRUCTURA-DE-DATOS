# EJERCICIO 9 — Contador de caracteres

class ContadorCaracteres:
    def __init__(self):
        self.textos = []

    def es_vocal(self, caracter):
        return caracter.lower() in "aeiouáéíóú"

    def analizar(self, texto):
        self.textos.append(texto)
        vocales = 0
        consonantes = 0
        digitos = 0

        for caracter in texto:
            if self.es_vocal(caracter):
                vocales += 1
            elif caracter.isalpha():
                consonantes += 1
            elif caracter.isdigit():
                digitos += 1

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "digitos": digitos
        }

    def texto_mas_largo(self):
        return max(self.textos, key=len)


contador = ContadorCaracteres()
print(contador.analizar("Hola 123"))
print(contador.analizar("Python es genial"))
print(contador.texto_mas_largo())
