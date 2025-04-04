class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __str__(self):
        return f"{self.__eurot}.{self.__sentit:02} eur"
    
    def __eq__(self, toinen):
        return self.__eurot == toinen.__eurot and self.__sentit == toinen.__sentit
    
    def __ne__(self, toinen):
        return self.__eurot != toinen.__eurot or self.__sentit != toinen.__sentit
    
    def __lt__(self, toinen):
        return self.__eurot < toinen.__eurot or (self.__eurot == toinen.__eurot and self.__sentit < toinen.__sentit)
    
    def __gt__(self, toinen):
        return self.__eurot > toinen.__eurot or (self.__eurot == toinen.__eurot and self.__sentit > toinen.__sentit)
    
    def __add__(self, toinen):
        sentit = self.__sentit + toinen.__sentit
        eurot = 0
        if sentit >= 100:
            eurot += 1
            sentit -= 100
        
        tulos = Raha(self.__eurot + toinen.__eurot + eurot, sentit)
        return tulos
    
    def __sub__(self,toinen):
        sentit = self.__sentit - toinen.__sentit
        eurot = 0
        if sentit < 0:
            eurot -= 1
            sentit += 100
            
        tulos = Raha(self.__eurot - toinen.__eurot + eurot, sentit)
        
        if tulos.__eurot > -1:
            return tulos
        else:
            raise ValueError ("negatiivinen tulos ei sallittu")
        
        
 
    
if __name__ == "__main__":
    e1 = Raha(3, 0)
    e2 = Raha(1, 0)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
    
    print(e5)