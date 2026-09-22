class AnalizadorPatrones:
    def __init__(self):
        self.ultimo_texto = ""

    def encontrar_palabras(self, texto, patron):
        self.ultimo_texto = texto
        palabras = texto.split()
        resultado = []
        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)
        return resultado

    def agrupar_por_longitud(self, texto):
        self.ultimo_texto = texto
        palabras = texto.split()
        resultado = {}
        for palabra in palabras:
            longitud = len(palabra)
            if longitud not in resultado:
                resultado[longitud] = []
            resultado[longitud].append(palabra)
        return resultado

    def palabras_unicas(self):
        return set(self.ultimo_texto.split())


ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato está aquí"))
print(ap.encontrar_palabras("el gato está aquí", "e"))
print(ap.palabras_unicas())
