# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kauppalista!
# Kirjoita ratkaisusi luokan alapuolelle!
class Kauppalista:
    def __init__(self):
        self.tuotteet = []

    def tuotteita(self):
        return len(self.tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))

    def tuote(self, n: int):
        return self.tuotteet[n - 1][0]

    def maara(self, n: int):
        return self.tuotteet[n - 1][1]

# ----------------------
# Tee ratkaisusi tähän:
# ----------------------
def tuotteita_yhteensa(lista: Kauppalista):
    y = []
    
    for i in range(1, lista.tuotteita()+1):
        #tuote = lista.tuote(i)
        maara = lista.maara(i)
        y.append(maara)
    
    return sum(y)
        



if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    

    print(tuotteita_yhteensa(lista))
   
