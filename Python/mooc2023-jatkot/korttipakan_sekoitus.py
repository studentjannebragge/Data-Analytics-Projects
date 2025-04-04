from random import shuffle

class Korttipakka:
    def __init__(self):
        self.__alusta_pakka()

    def __alusta_pakka(self):
        self.__pakka = []
        
        # Laitetaan kaikki kortit pakkaan
        maat = ["pata", "hertta", "risti", "ruutu"]
        for maa in maat:
            for numero in range(1, 14):
                self.__pakka.append((maa, numero))
                
        # Sekoitetaan pakka
        shuffle(self.__pakka)

    def jaa(self, korttien_maara: int):
        kasi = []
        
        # Siirretään pakasta ylimmät kortit käteen
        for i in range(korttien_maara):
            kasi.append(self.__pakka.pop())
        return kasi
    
if __name__ == "__main__":
    
    korttipakka = Korttipakka()
    kasi1 = korttipakka.jaa(5)
    print(kasi1)
    kasi2 = korttipakka.jaa(5)
    print(kasi2)