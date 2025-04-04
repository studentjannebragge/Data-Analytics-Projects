class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

class Huvipuistolaite:
    def __init__(self, nimi: str, pituusraja: int):
        self.kavijoita = 0
        self.nimi = nimi
        self.pituusraja = pituusraja

    def ota_kyytiin(self, henkilo: Henkilo):
        if henkilo.pituus >= self.pituusraja:
            self.kavijoita += 1
            print(f"{henkilo.nimi} pääsi kyytiin")
        else:
            print(f"{henkilo.nimi} liian lyhyt :(")

    def __str__(self):
        return f"{self.nimi} ({self.kavijoita} kävijää)"