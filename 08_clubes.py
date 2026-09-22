# EJERCICIO 8 — Clubes y participantes

class Clubes:
    def __init__(self):
        self.clubes = {}

    def crear(self, nombre_club):
        self.clubes[nombre_club] = []

    def inscribir(self, nombre_club, jugador):
        self.clubes[nombre_club].append(jugador)

    def club_mas_grande(self):
        return max(self.clubes, key=lambda club: len(self.clubes[club]))


clubes = Clubes()
clubes.crear("Norte")
clubes.crear("Sur")
clubes.inscribir("Norte", "Ana")
clubes.inscribir("Norte", "Luis")
clubes.inscribir("Sur", "Pedro")
print(clubes.clubes)
print(clubes.club_mas_grande())
