def sulut_tasapainossa(merkkijono: str):
    # Poistetaan kaikki muut merkit paitsi sulkumerkit
    merkkijono = ''.join(c for c in merkkijono if c in '()[]')
    
    if len(merkkijono) == 0:
        return True
    elif len(merkkijono) <= 2 and not ((merkkijono[0] == '(' and merkkijono[-1] == ')') or (merkkijono[0] == '[' and merkkijono[-1] == ']')):
        return False
    else:
        # poistetaan ensimmäinen ja viimeinen merkki
        return sulut_tasapainossa(merkkijono[1:-1])


if __name__ == "__main__":


      # ei kelpaa sillä erityyppiset sulut menevät ristiin
    ok = sulut_tasapainossa("([huono)]")
    print(ok)
    
    ok = sulut_tasapainossa("([([])])")
    print(ok)

    ok = sulut_tasapainossa("(python versio [3.7]) käytä tätä!")
    print(ok)

    # ei kelpaa sillä virheellinen loppusulku
    ok = sulut_tasapainossa("(()]")
    print(ok)


    # ei kelpaa sillä erityyppiset sulut menevät ristiin
    ok = sulut_tasapainossa("([huono)]")
    print(ok)