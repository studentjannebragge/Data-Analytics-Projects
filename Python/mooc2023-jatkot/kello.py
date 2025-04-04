import time
import os

# Tee ratkaisusi tähän:
class Kello:
    def __init__(self, tunnit: int, minuutit: int, sekunnit: int):
        self.sekunnit = sekunnit
        self.minuutit = minuutit
        self.tunnit = tunnit

    
    def tick(self):
        if self.sekunnit < 60:
            self.sekunnit += 1
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1
        if self.minuutit > 59:
            self.minuutit = 0
            self.sekunnit = 0
            self.tunnit += 1
        if self.tunnit > 23:
            self.minuutit = 0
            self.sekunnit = 0
            self.tunnit = 0
        
    def aseta(self, tunnit: int, minuutit: int):
        self.sekunnit = 0
        self.minuutit = minuutit
        self.tunnit = tunnit
            

    def __str__(self):
        if len(str(self.tunnit)) < 2 and len(str(self.minuutit)) < 2 and len(str(self.sekunnit)) < 2:
            return f'0{self.tunnit}:0{self.minuutit}:0{self.sekunnit}'
        if len(str(self.tunnit)) < 2 and len(str(self.minuutit)) < 2 and len(str(self.sekunnit)) == 2:
            return f'0{self.tunnit}:0{self.minuutit}:{self.sekunnit}'
        if len(str(self.tunnit)) < 2 and len(str(self.minuutit)) == 2 and len(str(self.sekunnit)) == 2:
            return f'0{self.tunnit}:{self.minuutit}:{self.sekunnit}'
        if len(str(self.tunnit)) == 2 and len(str(self.minuutit)) == 2 and len(str(self.sekunnit)) < 2:
            return f'{self.tunnit}:{self.minuutit}:0{self.sekunnit}'
        if len(str(self.tunnit)) < 2 and len(str(self.minuutit)) == 2 and len(str(self.sekunnit)) < 2:
            return f'0{self.tunnit}:{self.minuutit}:0{self.sekunnit}'
        if len(str(self.tunnit)) < 2 and len(str(self.minuutit)) == 2 and len(str(self.sekunnit)) == 2:
            return f'0{self.tunnit}:{self.minuutit}:{self.sekunnit}'
        if len(str(self.tunnit)) == 2 and len(str(self.minuutit)) < 2 and len(str(self.sekunnit)) < 2:
            return f'{self.tunnit}:0{self.minuutit}:0{self.sekunnit}'
        if len(str(self.tunnit)) == 2 and len(str(self.minuutit)) < 2 and len(str(self.sekunnit)) == 2:
            return f'{self.tunnit}:0{self.minuutit}:{self.sekunnit}'
        return f'{self.tunnit}:{self.minuutit}:{self.sekunnit}'
        
if __name__ == "__main__":
    
    kello = Kello(00, 00, 00)
    kello.aseta(12, 5)

    
    for i in range(3700, 0, -1):
        os.system('clear')
        print(kello)
        time.sleep(1)
        kello.tick()
        os.system('clear')