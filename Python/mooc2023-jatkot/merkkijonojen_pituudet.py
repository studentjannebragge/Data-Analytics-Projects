
def pituudet(merkkijonot: list):
    #funtio saa parametriksi listan merkkijonoja. Funktio palauttaa sanakirjan, jossa avaimina on listan merkkijonot ja arvoina merkkijonojen pituudet.
    return {merkki : len(merkki) for merkki in merkkijonot}




if __name__ == "__main__":

    sanalista = ["suo", "kuokka" , "python", "ja", "koodari"]

    sanojen_pituudet = pituudet(sanalista)
    print(sanojen_pituudet)