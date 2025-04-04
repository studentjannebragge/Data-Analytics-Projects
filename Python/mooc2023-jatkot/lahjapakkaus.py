class Lahja:
    def __init__(self, nimi: str, paino: int):
        self.nimi = nimi
        self.paino = paino
    def __str__(self):
        return f'{self.nimi} ({self.paino} kg)'
    
class Pakkaus:
    def __init__(self):
        self.lahjat = []
    
    def lisaa_lahja(self, lahja: Lahja):
        self.lahjat.append(lahja)
    
    def yhteispaino(self):
        paino = 0
        for each in self.lahjat:
            paino += each.paino
        return paino
        


if __name__ == "__main__":
    
    kirja = Lahja("Aapiskukko", 2)

    pakkaus = Pakkaus()
    pakkaus.lisaa_lahja(kirja)
    print(pakkaus.yhteispaino())