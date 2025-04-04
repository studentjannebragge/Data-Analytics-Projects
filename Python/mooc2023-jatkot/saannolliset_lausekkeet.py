import re

def on_viikonpaiva(merkkijono: str) -> bool:
    viikonpaivat = ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su']
    for paiva in viikonpaivat:
        if re.search(r'\b' + paiva + r'\b', merkkijono):
            return True
    return False

def kaikki_vokaaleja(merkkijono: str) -> bool:
    if re.fullmatch(r'[aeiouyäöå]*', merkkijono):
        return True
    return False

def kellonaika(merkkijono: str):
    if re.fullmatch(r'(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', merkkijono):
        return True
    return False
    


if __name__ == "__main__":
    print(kellonaika("12:43:01"))
    print(kellonaika("AB:01:CD"))
    print(kellonaika("17:59:59"))
    print(kellonaika("33:66:77"))