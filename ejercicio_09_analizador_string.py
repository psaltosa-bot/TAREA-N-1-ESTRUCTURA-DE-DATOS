class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        vocales = 0
        consonantes = 0
        digitos = 0
        for caracter in texto:
            if caracter.isdigit():
                digitos += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    vocales += 1
                else:
                    consonantes += 1
        return {'vocales': vocales, 'consonantes': consonantes, 'digitos': digitos}


astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))
