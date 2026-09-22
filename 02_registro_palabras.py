# EJERCICIO 2 — Registro de palabras

class RegistroPalabras:
    def __init__(self):
        self.palabras = []
        self.unicas = set()

    def guardar(self, palabra):
        self.palabras.append(palabra)
        self.unicas.add(palabra)

    def total_unicas(self):
        return len(self.unicas)

    def guardar_varias(self, *palabras):
        for palabra in palabras:
            self.guardar(palabra)


registro = RegistroPalabras()
registro.guardar_varias("sol", "luna", "sol", "mar", "luna")
print(registro.palabras)
print(registro.total_unicas())
