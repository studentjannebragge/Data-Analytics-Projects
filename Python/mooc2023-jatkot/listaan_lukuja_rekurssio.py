def listaan_lukuja(luvut: list):
    #lisää listaan lukuja niin kauan, kunnes listan pituus on viidellä jaollinen.
    #Jokainen listaan lisättävä luku on aina yhden suurempi kuin listan viimeinen luku.
    if len(luvut) % 5 != 0:
        luvut.append(luvut[-1] + 1)
        listaan_lukuja(luvut)
    
    
if __name__ == "__main__":
    
    luvut = [1,3,4,5,10,11]
    listaan_lukuja(luvut)
    print(luvut)