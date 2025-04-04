# Tee ratkaisusi tähän:
import math

class Sarja:
    def __init__(self, nimi: str, kaudet: int, genret: list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.genret = genret
        self.arvostelut = []
        self.arvostelut_ka = 0
        
    
    def __str__(self):
        tulostus_genret = ", ".join(self.genret)
        if len(self.arvostelut) > 0:
            return f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {tulostus_genret}\narvosteluja {len(self.arvostelut)}, keskisarvo {self.arvostelut_ka:.1f} pistettä"
        else:
            return f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {tulostus_genret}\nei arvosteluja"
    
    
    def arvostele(self, arvosana: int):
        if arvosana > -1 and arvosana < 6:
            self.arvostelut.append(arvosana)
        else:
            raise ValueError("arvosanan oltava väliltä 0 - 5")
            #print("arvosanan oltava väliltä 0 - 5")
        
        self.arvostelut_ka = sum(self.arvostelut) / len(self.arvostelut)
        
    
    def sisaltaa_genren(genre: str, sarjat: list):
        pass


if __name__ == "__main__":

    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]
    
    def arvosana_vahintaan(arvosana: float, sarjat: list):
        for sarja in sarjat:
            if sarja.arvostelut_ka > arvosana:
                print(sarja.nimi)
    
    print("arvosana vähintään 4.5:")
    arvosana_vahintaan(4.5, sarjat)  

    def sisaltaa_genren(genre: str, sarjat: list):
        for sarja in sarjat:
            if genre in sarja.genret:
                print(sarja.nimi)
    print()
    print("genre Comedy:")
    sisaltaa_genren("Comedy", sarjat)
    
    