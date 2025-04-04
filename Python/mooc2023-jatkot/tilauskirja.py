class Tehtava:
    id = 1
    
    def __init__(self, kuvaus: str, koodari: str, tyomaara: int):
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara
        self.valmis = False
        self.id = Tehtava.id
        Tehtava.id += 1
        
    def on_valmis(self):
        self.valmis == True
        return self.valmis
    
    def merkkaa_valmiiksi(self):
        self.valmis = True
        return self.valmis
    
    def __str__(self):
        if self.valmis == True:
            return f'{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} VALMIS'
        else:
            return f'{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} EI VALMIS'


class Tilauskirja:
    def __init__(self):
        self.tilaukset = []
        
    def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):
        self.tilaukset.append(Tehtava(kuvaus, koodari, tyomaara))
    
    def kaikki_tilaukset(self):
        return self.tilaukset
    
    def koodarit(self):
        koodarit = set(tilaus.koodari for tilaus in self.tilaukset)
        list_koodarit = list(koodarit)
        return list_koodarit
        
    def merkkaa_valmiiksi(self, id: int):
        tilaukset = [tilaus.id for tilaus in self.tilaukset]
        if id not in tilaukset:
            raise ValueError("Tilausta ei löydy!")
        else:
            for tilaus in self.tilaukset:
                if tilaus.id == id:
                    tilaus.valmis = True
    
    def valmiit_tilaukset(self):
        return [tilaus for tilaus in self.tilaukset if tilaus.valmis == True]
    
    def ei_valmiit_tilaukset(self):
        return [tilaus for tilaus in self.tilaukset if tilaus.valmis == False]
    
    def koodarin_status(self, koodari: str):
        koodarit = [k.koodari for k in self.tilaukset]
        if koodari not in koodarit:
            raise ValueError("Koodaria ei löydy!")
        else:
            koodarin_tehtavat = [k for k in self.tilaukset if k.koodari == koodari]
            valmiit = []
            ei_valmis = []
            h_tekematta = 0
            h_tehty = 0
            
            for tieto in koodarin_tehtavat:
                if tieto.valmis == True:
                    valmiit.append(tieto)
                else:
                    ei_valmis.append(tieto)
                    
            for tieto in valmiit:
                h_tehty += tieto.tyomaara
            
            for tieto in ei_valmis:
                h_tekematta += tieto.tyomaara
                    
            t = [len(valmiit), len(ei_valmis), h_tehty, h_tekematta]
            return tuple(t)
    
if __name__ == "__main__":
    
    tilaukset = Tilauskirja()
    tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Antti", 25)
    tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    tilaukset.lisaa_tilaus("tee uusi facebook", "Erkki", 1000)

    tilaukset.merkkaa_valmiiksi(1)
    tilaukset.merkkaa_valmiiksi(2)

    status = tilaukset.koodarin_status("Antti")
    print(status)