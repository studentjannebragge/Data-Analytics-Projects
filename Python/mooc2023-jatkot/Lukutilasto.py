# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.sum = 0
        self.maara = 0
        self.yhteensa = 0
        self.ka = 0

    def lisaa_luku(self, luku:int):
        if luku != -1:
            self.lukuja += 1
            self.sum += luku
        

    def lukujen_maara(self):
        self.maara = self.lukuja
        maara =  self.maara
        return maara
    
    def summa(self):
        self.yhteensa = self.sum
        yhteensa = self.yhteensa
        return yhteensa
    
    def keskiarvo(self):
        maara = self.lukuja
        if self.lukuja > 0:
            self.ka = self.yhteensa / maara
            keskiarvo = self.ka
            return keskiarvo
        
        keskiarvo = 0
        return keskiarvo

tilasto = Lukutilasto()
parittomat_tilasto = Lukutilasto()
parilliset_tilasto = Lukutilasto()
#tilasto.lisaa_luku(3)
#tilasto.lisaa_luku(5)
#tilasto.lisaa_luku(1)
#tilasto.lisaa_luku(1)
#print("Lukujen määrä:", tilasto.lukujen_maara())
#print("Summa:", tilasto.summa())
#print("Keskiarvo:", tilasto.keskiarvo())



def laske_yhteen():
    def parittomat(luku: int):
        if luku % 2 != 0:
            parittomat_tilasto.lisaa_luku(luku)
    
    def parilliset(luku: int):
        if luku % 2 == 0:
            parilliset_tilasto.lisaa_luku(luku)   

            
   
    
    while True:
        try:
            luku = int(input("Anna lukuja: "))
        except ValueError:
            print("Et syöttänyt mitään tai syöttämäsi ei ollut luku")
        if luku == -1:
            break
        else:
            tilasto.lisaa_luku(luku)
            parittomat(luku)
            parilliset(luku)        
        
    print("Summa:", tilasto.summa())
    print("Keskiarvo:", tilasto.keskiarvo())
    print("Parillisten summa:", parilliset_tilasto.summa())
    print("Parittomien summa:", parittomat_tilasto.summa())
    
laske_yhteen()

