
def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    
    
    with open(tiedoston_nimi, 'r') as tiedosto:
        sanat = tiedosto.read().split()
        for each in sanat:
            if each[-1] in ".,!?":
                sanat.remove(each)
                sanat.append(each[:-1])

        
        #return {sana: lkm for sana, lkm in sanat.items() if lkm >= raja}
        
        merkkimäärät = {kirjain : sanat.count(kirjain) for kirjain in sanat if sanat.count(kirjain) >= raja}
        return merkkimäärät
        



if __name__ == "__main__":


    print(yleisimmat_sanat("programming.txt", 1))