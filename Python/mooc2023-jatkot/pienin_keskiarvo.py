def keskiarvo(henkilo: dict):
    summa = henkilo["tulos1"]+henkilo["tulos2"]+henkilo["tulos3"]
    return summa/3
 
def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    pienin_henkilo = henkilo1
 
    if keskiarvo(henkilo2) < keskiarvo(pienin_henkilo):
        pienin_henkilo = henkilo2
 
    if keskiarvo(henkilo3) < keskiarvo(pienin_henkilo):
        pienin_henkilo = henkilo3
 
    return pienin_henkilo