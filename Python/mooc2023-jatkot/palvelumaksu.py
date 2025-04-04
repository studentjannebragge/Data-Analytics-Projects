class Pankkitili:
    def __init__(self, tilinomistaja: str, tilinumero: int, saldo: float):
        self.__tilinomista = tilinomistaja
        self.__tilinumero = tilinumero
        self.__saldo = saldo
        
    def talleta(self, summa: float):
        self.__saldo += summa
        pm = self.__palvelumaksu()
        self.__saldo -= pm
    
    def nosta (self, summa: float):
        if self.__saldo > summa:
            self.__saldo -= summa
            pm = self.__palvelumaksu()
            self.__saldo -= pm
        else:
            raise ValueError("tilillä ei ole tarpeeksi rahaa")
    
    @property
    def saldo(self):
        return self.__saldo
    
    def __palvelumaksu(self):
        palvelumaksu = self.saldo / 100
        return palvelumaksu


if __name__ == "__main__":
    tili = Pankkitili("Raimo Rahakas", "12345-6789", 1000)
    tili.nosta(100)
    print(tili.saldo)
    tili.talleta(100)
    print(tili.saldo)