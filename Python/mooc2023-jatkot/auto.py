# TEE RATKAISUSI TÄHÄN:
class Auto:
    def __init__(self):
        self.__bensaa = 0
        self.__ajetutkm = 0
    
    def tankkaa(self):
        if self.__bensaa == 0:
            self.__bensaa += 60
    
    def aja(self, km: int):
        if km > self.__bensaa:
            self.__ajetutkm += self.__bensaa
            self.__bensaa -= self.__bensaa
    
        else:
            self.__ajetutkm += km
            self.__bensaa -= km
    
    def __str__(self) -> str:
        return f'Auto: ajettu {self.__ajetutkm} km, bensaa {self.__bensaa} litraa'
    
    
    
if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)