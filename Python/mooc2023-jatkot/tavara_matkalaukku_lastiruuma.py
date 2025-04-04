
class Tavara:
    def __init__(self, nimi: str, paino: int):
        self.__nimi = nimi
        self.__paino = paino
    
    def nimi(self):
        return self.__nimi
    
    def paino(self):
        return self.__paino
    
    def __str__(self):
        return f"{self.__nimi} ({self.__paino} kg)"
    
    
class Matkalaukku:
    def __init__(self, maxpaino: int):
        self.__maxpaino = maxpaino
        self.__tavarat = []
        self.__nykyinen_paino = 0
        
    def lisaa_tavara(self, tavara: Tavara):
        if self.__nykyinen_paino + tavara.paino() <= self.__maxpaino:
            self.__tavarat.append(tavara)
            self.__nykyinen_paino += tavara.paino()
            
    def tulosta_tavarat(self):
        for each in self.__tavarat:
            print(each)
            
    def raskain_tavara(self):
        if len(self.__tavarat) == 0:
            return None
        else:
            return max(self.__tavarat, key=lambda tavara: tavara.paino())
        
    def paino(self):
        return self.__nykyinen_paino
    
    def __str__(self):
        if len(self.__tavarat) == 1:
            return f"{len(self.__tavarat)} tavara ({self.__nykyinen_paino} kg)"
        else:
            return f"{len(self.__tavarat)} tavaraa ({self.__nykyinen_paino} kg)"        

class Lastiruuma:
    def __init__(self, maxpaino: int):
        self.__maxpaino = maxpaino
        self.__yhteispaino = 0
        self.__lastiruuma = []
    
    def lisaa_matkalaukku(self, matkalaukku: Matkalaukku):
        if self.__yhteispaino + matkalaukku.paino() <= self.__maxpaino:
            self.__lastiruuma.append(matkalaukku)
            self.__yhteispaino += matkalaukku.paino()
    
    def tulosta_tavarat(self):
        for matkalaukku in self.__lastiruuma:
            matkalaukku.tulosta_tavarat()
    
    def __str__(self):
        if len(self.__lastiruuma) == 1:
            return f'{len(self.__lastiruuma)} matkalaukku, tilaa {self.__maxpaino - self.__yhteispaino} kg'
        else:
            return f'{len(self.__lastiruuma)} matkalaukkua, tilaa {self.__maxpaino - self.__yhteispaino} kg'  
            
        
    
    
if __name__ == "__main__":
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma = Lastiruuma(1000)
    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)

    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()