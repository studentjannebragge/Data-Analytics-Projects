from datetime import date

def vuodet_listaan(vuodet: list):
    y = []
    
    
    for each in vuodet:
        y.append(each.year)
        
    y.sort()
    return y



if __name__ == "__main__":



    paiva1 = date(2019, 2, 3)
    paiva2 = date(2006, 10, 10)
    paiva3 = date(1900, 1, 1)
    
    vuodet = [paiva1, paiva2, paiva3]


    vuodet = vuodet_listaan(vuodet)
    print(vuodet)