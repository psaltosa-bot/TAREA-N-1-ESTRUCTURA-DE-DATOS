class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        resultado = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria not in resultado:
                resultado[categoria] = []
            resultado[categoria].append(edad)
        self.grupos = resultado
        return resultado

    def edad_promedio_categoria(self, categoria):
        if categoria not in self.grupos or not self.grupos[categoria]:
            return 0
        return sum(self.grupos[categoria]) / len(self.grupos[categoria])


ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))
print(ae.edad_promedio_categoria("adulto"))
