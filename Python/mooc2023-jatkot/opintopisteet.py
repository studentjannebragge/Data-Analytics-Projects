from functools import reduce

class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"

def kaikkien_opintopisteiden_summa(suoritukset: list):
    summa = reduce(lambda summa, alkio: summa + alkio.opintopisteet, suoritukset, 0)
    return summa

def hyvaksyttyjen_opintopisteiden_summa(suoritukset: list):
    hyvaksytyt = filter(lambda s : s.arvosana >= 1, suoritukset)
    hyvaksytyt_op = reduce(lambda summa, alkio: summa + alkio.opintopisteet, hyvaksytyt, 0)
    return hyvaksytyt_op
    
def keskiarvo(suoritukset: list):
    hyvaksytyt = list(filter(lambda s : s.arvosana >= 1, suoritukset))
    hyvaksytyt_op = reduce(lambda summa, alkio: summa + alkio.arvosana, hyvaksytyt, 0)
    ka = hyvaksytyt_op / len(hyvaksytyt)
    return round(ka, 1)

if __name__ == "__main__":
    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = keskiarvo([s1, s2, s3])
    print(summa)