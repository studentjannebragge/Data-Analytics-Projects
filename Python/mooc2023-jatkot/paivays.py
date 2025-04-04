class Paivays:
    def __init__(self, paiva: int, kuukausi: int, vuosi: int):
        self.__paiva = paiva
        self.__kuukausi = kuukausi
        self.__vuosi = vuosi
    
    def __str__(self):
        return f"{self.__paiva}.{self.__kuukausi}.{self.__vuosi}"
    
    def __eq__(self, toinen):
        return self.__paiva == toinen.__paiva and self.__kuukausi == toinen.__kuukausi and self.__vuosi == toinen.__vuosi
    
    def __ne__(self, toinen):
        return self.__paiva != toinen.__paiva or self.__kuukausi != toinen.__kuukausi or self.__vuosi != toinen.__vuosi
    
    def __lt__(self, toinen):
        if self.__vuosi < toinen.__vuosi:
            return True
        elif self.__vuosi == toinen.__vuosi:
            if self.__kuukausi < toinen.__kuukausi:
                return True
            elif self.__kuukausi == toinen.__kuukausi:
                return self.__paiva < toinen.__paiva
        return False
    
    def __gt__(self, toinen):
        
        if self.__vuosi > toinen.__vuosi:
            return True
        elif self.__vuosi == toinen.__vuosi:
            if self.__kuukausi > toinen.__kuukausi:
                return True
            elif self.__kuukausi == toinen.__kuukausi:
                return self.__paiva > toinen.__paiva
        return False
    
    def __add__(self, toinen):
        vuodet = toinen // 360
        kuukaudet = (toinen % 360) // 30
        paivat_jaljella = toinen % 30
        
        paiva = self.__paiva + paivat_jaljella
        if paiva > 30:
            kuukaudet += 1
            paiva -= 30
        
        kuukausi = self.__kuukausi + kuukaudet
        if kuukausi > 12:
            vuodet += 1
            kuukausi -= 12
            
        vuosi = self.__vuosi + vuodet
       
        uusi_pvm = Paivays(paiva, kuukausi, vuosi)
        return uusi_pvm
    
    def __sub__(self, toinen):
        paivat_s = self.__paiva + self.__kuukausi * 30 + self.__vuosi * 360
        paivat_t = toinen.__paiva + toinen.__kuukausi * 30 + toinen.__vuosi * 360
        
        summa = paivat_t - paivat_s
        
        return abs(summa)
        
    
if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)