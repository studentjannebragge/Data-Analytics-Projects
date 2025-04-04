import time
import os

# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.kymppisekunnit = 0
        self.minuutit = 0
        self.kymppiminuutit = 0
    
    def tick(self):
        if self.sekunnit < 10:
            self.sekunnit += 1
        if self.sekunnit == 10:
            self.sekunnit = 0
            self.kymppisekunnit += 1
        if self.kymppisekunnit > 5:
            self.minuutit += 1
            self.kymppisekunnit = 0
            self.sekunnit = 0
        if self.minuutit > 9:
            self.kymppiminuutit += 1
            self.minuutit = 0
            self.kymppisekunnit = 0
            self.sekunnit = 0
        if self.kymppiminuutit > 5:
            self.kymppiminuutit = 0
            self.minuutit = 0
            self.kymppisekunnit = 0
            self.sekunnit = 0
            

    def __str__(self):
        return f"{self.kymppiminuutit}{self.minuutit}:{self.kymppisekunnit}{self.sekunnit}"
        
        
if __name__ == "__main__":
    
    kello = Sekuntikello()
    
    for i in range(3600, 0, -1):
        os.system('clear')
        print(kello)
        time.sleep(1)
        kello.tick()
        os.system('clear')
        
        