import random

def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    for i in (range(maara)):
       sana = ''.join(random.choice(kirjaimet) for i in range(pituus))
       yield sana 



if __name__ == "__main__":
    sanagen = sanageneraattori("abcdefg", 3, 5)
    for sana in sanagen:
        print(sana)    