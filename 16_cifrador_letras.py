# EJERCICIO 16 — Cifrador de letras

class CifradorLetras:
    def __init__(self):
        self.registro = {}

    def mover_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra

        base = ord("a")
        posicion = ord(letra.lower()) - base
        nueva = (posicion + desplazamiento) % 26
        resultado = chr(base + nueva)

        if letra.isupper():
            resultado = resultado.upper()

        return resultado

    def cifrar(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.mover_letra(letra, desplazamiento)

        self.registro[palabra] = resultado
        return resultado

    def historial(self):
        return self.registro


cifrador = CifradorLetras()
print(cifrador.cifrar("Python", 3))
print(cifrador.cifrar("Hola", 2))
print(cifrador.historial())
