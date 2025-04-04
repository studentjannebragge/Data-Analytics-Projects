# TEE RATKAISUSI TÄHÄN:
from math import sqrt

def neliojuuret(luvut: list):
    return [sqrt(luku) for luku in luvut]

#neliojuuret = [sqrt(luku) for luku in rivit]

if __name__ == "__main__":

    rivit = neliojuuret([1,2,3,4])
    for rivi in rivit:  
        print(rivi)
        
