# EJERCICIO 17 — Clasificador de edades

class ClasificadorEdades:
    def categoria(self, edad):
        if edad <= 12:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar(self, *edades):
        resultado = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

        for edad in edades:
            resultado[self.categoria(edad)].append(edad)

        return resultado

    def promedio_categoria(self, edades):
        if not edades:
            return 0
        return sum(edades) / len(edades)


clasificador = ClasificadorEdades()
grupos = clasificador.agrupar(8, 15, 25, 70, 10, 18)
print(grupos)
print(clasificador.promedio_categoria(grupos["adulto"]))
