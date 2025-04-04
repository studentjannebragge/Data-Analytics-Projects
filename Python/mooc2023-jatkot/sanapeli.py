import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")

class PisinSana(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1
        elif len(pelaaja1_sana) < len(pelaaja2_sana):
            return 2
        else:
            return 0

class EnitenVokaaleja(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
        
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        vokaalit = "'aeiouyäö'"
        
        pelaaja1_vokaalit = sum(1 for kirjain in pelaaja1_sana if kirjain in vokaalit)
        pelaaja2_vokaalit = sum(1 for kirjain in pelaaja2_sana if kirjain in vokaalit)
        
        if pelaaja1_vokaalit > pelaaja2_vokaalit:
            return 1
        elif pelaaja1_vokaalit < pelaaja2_vokaalit:
            return 2
        else:
            return 0

class KiviPaperiSakset(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
    
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        
        sanat = ["kivi", "paperi", "sakset"]
        if pelaaja1_sana not in sanat:
            pelaaja1_sana = "epäkelpo"
        
        if pelaaja2_sana not in sanat:
            pelaaja2_sana = "epäkelpo"
        
        
        
        if pelaaja1_sana == "kivi" and pelaaja2_sana == "sakset":
            return 1
        elif pelaaja1_sana == "sakset" and pelaaja2_sana == "paperi":
            return 1
        elif pelaaja1_sana == "paperi" and pelaaja2_sana == "kivi":
            return 1
        elif pelaaja1_sana == pelaaja2_sana and pelaaja1_sana != "epäkelpo":
            pass
        elif pelaaja1_sana == "epäkelpo" and pelaaja2_sana != "epäkelpo":
            return 2
        elif pelaaja2_sana == "epäkelpo" and pelaaja1_sana != "epäkelpo":
            return 1
        elif pelaaja1_sana == "epäkelpo" and pelaaja2_sana == "epäkelpo":
            pass
        else:
            return 2 


if __name__ == "__main__":

    p = KiviPaperiSakset(4)
    p.pelaa()