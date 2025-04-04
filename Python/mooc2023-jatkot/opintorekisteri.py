class Opintorekisteri():
    def __init__(self):
        self.__arvosanat = {}
   
        
    def lisaa_arvosana(self, kurssinimi: str, opintopisteet: int, arvosana: int):
        if not kurssinimi in self.__arvosanat:
            #muodostetaan olio sanakirjaan
            self.__arvosanat[kurssinimi] = Opinto(kurssinimi, opintopisteet, arvosana)
        self.__arvosanat[kurssinimi].vaihda_arvosana(arvosana)
            
   
    
    def hae_arvosana(self, kurssinimi: str):
        if not kurssinimi in self.__arvosanat:
            return None
        return self.__arvosanat[kurssinimi]

    
class Opinto():
    def __init__(self, kurssinimi: str, opintopisteet: int, arvosana: int):
        self.__kurssinimi = kurssinimi
        self.__opintopisteet = opintopisteet
        self.__arvosana = arvosana
    
    def nimi(self):
        return self.nimi
    
    def arvosana(self):
        return self.arvosana
    
    def opintopisteet(self):
        return self.opintopisteet
    
    def vaihda_arvosana(self, arvosana):
        if self.__arvosana < arvosana:
            self.__arvosana = arvosana
    
    def __str__(self) -> str:
        return f'{self.__kurssinimi} ({self.__opintopisteet} op) arvosana {self.__arvosana}'
 

class OpintorekisteriSovellus():
    def __init__(self):
        self.__arvosanarekisteri = Opintorekisteri()
        
    def ohje(self):
        #print("komennot:")
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("0 lopetus")
        
    def arvosanan_lisays(self):
        kurssinimi = input("kurssi: ")
        arvosana = input("arvosana: ")
        opintopisteet = input("opintopisteet: ")
        self.__arvosanarekisteri.lisaa_arvosana(kurssinimi, opintopisteet, arvosana)
        
    def arvosanan_haku(self):
        kurssinimi = input("kurssi: ")
        tiedot = self.__arvosanarekisteri.hae_arvosana(kurssinimi)
        if tiedot == None:
            print("ei suoritusta")
            return
        print(tiedot)
    
    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input(("komento: "))
            if komento == "0":
                break
            elif komento == "1":
                self.arvosanan_lisays()
            elif komento == "2":
                self.arvosanan_haku()
            else:
                self.ohje()
     
     
 
 
 
sovellus = OpintorekisteriSovellus()
sovellus.suorita()
    

      
    
    
"""    
    
    
    
    
    1 lisää suoritus
    2 hae suoritus
    3 tilastot
    0 lopetus
"""