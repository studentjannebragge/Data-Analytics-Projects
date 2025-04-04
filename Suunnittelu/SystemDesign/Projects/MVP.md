Tässä tapauksessa MVP olisi järjestelmän yksinkertaisin mutta toimiva versio, joka täyttää annettujen vaatimusten perusominaisuudet. Seuraavassa kuvailen tarkemmin, millainen MVP voisi olla:

---

### **1. Mobiilisovellus (asiakkaiden käyttöön)**
MVP:n tavoite on mahdollistaa kuitin tietojen nopea ja helppo käsittely. Tärkeimmät ominaisuudet:

1. **Kuitin skannaus**
   - Käyttäjä ottaa kuvan kuitista sovelluksen kameratoiminnolla.
   - Kuva tallennetaan väliaikaisesti ja käsitellään OCR-teknologialla.
   
2. **Tiedon poiminta**
   - OCR tunnistaa seuraavat tiedot:
     - Päivämäärä
     - Laskun aihe (esim. "lounas" tai "toimistotarvikkeet")
     - Summa
     - ALV-luokka
   - Käyttäjä voi tarkistaa ja korjata tietoja, jos tunnistuksessa tapahtuu virheitä.

3. **Kulukorvauslomake**
   - Poimitut tiedot siirretään esitäytettyyn lomakkeeseen, jonka käyttäjä voi tallentaa tai lähettää sähköpostitse.

4. **Käyttöliittymä**
   - Erittäin yksinkertainen ja intuitiivinen käyttöliittymä, joka ohjaa käyttäjää vaihe vaiheelta.

---

### **2. Taustajärjestelmä (yrityksen hallintaan)**
Taustajärjestelmä keskittyy MVP-vaiheessa perushallintatoimintoihin:

1. **Käyttäjä- ja sovellushallinta**
   - Näkyvyys rekisteröityihin käyttäjiin ja heidän käyttämäänsä sovellusversioon.
   - Yksinkertainen kirjautumisjärjestelmä, jolla ylläpitäjät pääsevät hallintapaneeliin.

2. **Käyttötilastot**
   - Kuittien skannausten kokonaismäärä tietyn ajanjakson aikana.
   - Keskimääräinen kuittien määrä per käyttäjä.
   - Tunnistusvirheiden lukumäärä ja yleisimmät ongelmat.

3. **Raportointi**
   - Perustason graafit ja tilastot hallintapaneelissa (esim. pylväsdiagrammi käsitellyistä kuiteista kuukauden aikana).

---

### **3. Teknologiset valinnat**
MVP:n teknologioiden tulee mahdollistaa nopea kehitys ja perustason toiminnallisuus:

1. **Mobiilisovellus**
   - Kehitystyökalut: React Native tai Flutter (tuki sekä Androidille että iOS:lle).
   - Käytetään valmiita kirjastoja OCR-tunnistukseen, kuten Google Vision API tai Tesseract.

2. **Taustajärjestelmä**
   - Backend: Node.js tai Python (Django/Flask).
   - Tietokanta: PostgreSQL (relaatiotietokanta) tai Firebase (pilvipohjainen).
   - Pilvi-infrastruktuuri: AWS, Azure tai Google Cloud.

3. **Tietoturva**
   - Käyttäjätiedot ja kuvat salataan, ja tiedonsiirrossa käytetään HTTPS-protokollaa.

---

### **4. Käyttäjäpalautteen kerääminen**
- Sovellus julkaistaan rajatulle käyttäjäryhmälle (beta-testaus).
- Käyttäjiltä kerätään palautetta sovelluksen käytettävyydestä, virheistä ja parannusehdotuksista.
- Taustajärjestelmä kerää analytiikkaa käytöstä ja tunnistuksen tarkkuudesta.

---

