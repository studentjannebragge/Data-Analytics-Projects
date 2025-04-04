class ListaApuri:
    def __init__(self, luvut: list):
        self.luvut = luvut
        
    
    @classmethod
    def suurin_frekvenssi(cls, lista: list):
        maarat = {}
        
        for alkio in lista:
            if alkio in maarat:
                maarat[alkio] += 1
            else:
                maarat[alkio] = 1
        suurin = max(maarat, key=maarat.get)
        
        return suurin
    
    @classmethod
    def tuplia(cls, lista: list):
        useasti = []
        maarat = {}
        
        for alkio in lista:
            if alkio in maarat:
                maarat[alkio] += 1
            else:
                maarat[alkio] = 1
        
        for alkio, maara in maarat.items():
            if maara > 1:
                useasti.append(alkio)
        
        return len(useasti)    
        

    
    
if __name__ == "__main__":
   
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]

    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut)) 