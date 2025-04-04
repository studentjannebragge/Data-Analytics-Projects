class Havaintoasema:
    def __init__(self, asema: str):
        self.__asema = asema
        self.__havainto = []
        self.__havainnot_maara = 0
        
    
    def lisaa_havainto(self, havainto: str):
        if havainto != "":
            self.__havainto.append(havainto)
            self.__havainnot_maara += 1
        else: 
            raise ValueError("Havainto ei voi olla tyhjä!")
    
    
    def viimeisin_havainto(self):
        if len(self.__havainto) == 0:
            a = " "
            return a
        else:
            viimesin = len(self.__havainto) - 1
            return self.__havainto[viimesin]
    
    def havaintojen_maara(self):
        return self.__havainnot_maara
    
    def __str__(self):
        return f'{self.__asema}, {self.__havainnot_maara} havaintoa'
    
if __name__ == "__main__":
    
    asema = Havaintoasema("Kumpula")
    asema.lisaa_havainto("Sadetta 10mm")
    asema.lisaa_havainto("Aurinkoista")
    print(asema.viimeisin_havainto())

    asema.lisaa_havainto("Ukkosta")
    print(asema.viimeisin_havainto())

    print(asema.havaintojen_maara())
    print(asema)