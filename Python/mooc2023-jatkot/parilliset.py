def parilliset(alku: int, maksimi: int):

    for luku in range(alku, maksimi + 1):    
        
        if luku % 2 == 0:
            yield luku

if __name__ == "__main__":

    luvut = parilliset(2, 10)
    for luku in luvut:
        print(luku)
