class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

def jarjestys_pituus(alkio: Kiipeilyreitti):
    return alkio.pituus

def pituuden_mukaan(reitit: list):
    return sorted(reitit, key=jarjestys_pituus, reverse=True)

def jarjestys_vaikeus(alkio: Kiipeilyreitti):
    return alkio.grade

def vaikeuden_mukaan(reitit: list):
    return sorted(reitit, key=lambda reitit: (reitit.grade, reitit.pituus), reverse=True)
    

if __name__ == "__main__":
    
    r1 = Kiipeilyreitti("Kantti", 38, "6A+")
    r2 = Kiipeilyreitti("Smooth operator", 11, "7A")
    r3 = Kiipeilyreitti("Syncro", 14, "8C+")
    r4 = Kiipeilyreitti("Pieniä askelia", 12, "6A+")

    reitit = [r1, r2, r3, r4]
    for reitti in vaikeuden_mukaan(reitit):
        print(reitti)