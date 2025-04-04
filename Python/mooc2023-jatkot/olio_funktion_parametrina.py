class Opiskelija:
    def __init__(self, nimi: str, opiskelijanumero: str):
        self.nimi = nimi
        self.opiskelijanumero = opiskelijanumero

    def __str__(self):
        return f"{self.nimi} ({self.opiskelijanumero})"

# Huomaa, että tyyppivihjeenä käytetään nyt oman luokan nimeä
def muuta_nimi(opiskelija: Opiskelija):
    opiskelija.nimi = "Olli Opiskelija"
    
def muuta_numero(numero: Opiskelija):
    numero.opiskelijanumero = ("999999")

# Luodaan opiskelijaolio
olli = Opiskelija("Olli Oppilas", "12345")

print(olli)
muuta_nimi(olli)
print(olli)
muuta_numero(olli)
print(olli)