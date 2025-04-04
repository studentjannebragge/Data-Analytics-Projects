# Tee ratkaisusi tähän:

class Henkilo:
    
    def __init__(self, nimi: str):
        self.nimi = nimi
        
    def anna_etunimi(self):
        nimi = self.nimi 
        etunimi = nimi.split()[0]
        return etunimi
        
    def anna_sukunimi(self):
        nimi = self.nimi
        sukunimi = nimi.split()[1]
        return sukunimi


if __name__ == "__main__":
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())
    print(pekka.anna_sukunimi())

    pauli = Henkilo("Pauli Pythonen")
    print(pauli.anna_etunimi())
    print(pauli.anna_sukunimi())