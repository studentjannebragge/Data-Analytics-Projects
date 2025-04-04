Tässä on tehtävänannon pohjalta laadittu **stakeholder map**:

---

### **1. Sidosryhmien tunnistaminen**
Sidosryhmät jaetaan seuraaviin pääryhmiin tehtävänannon perusteella:

#### **1.1 Sisäiset sidosryhmät (projektitiimin sisällä)**
- **Projektin johto**: Vastaa projektin etenemisestä, budjetista ja aikataulusta.
- **Kehittäjät**: Toteuttavat mobiilisovelluksen ja taustajärjestelmän.
- **Tekoälyasiantuntijat**: Kehittävät kuitin tunnistukseen liittyvän OCR-teknologian.
- **UX-suunnittelijat**: Suunnittelevat käyttäjäystävällisen mobiilisovelluksen ja hallintapaneelin.
- **Testaajat**: Vastaavat järjestelmän laadunvarmistuksesta.

#### **1.2 Ulkoiset sidosryhmät**
- **Tilitoimiston johto (asiakasyritys)**: Päätöksentekijät, jotka ovat tilanneet projektin.
- **Tilitoimiston asiakkaat**: Loppukäyttäjät, jotka käyttävät mobiilisovellusta kulukorvausten ja matkalaskujen tekemiseen.
- **IT-osasto (asiakasyritys)**: Vastaa mobiilisovelluksen ja taustajärjestelmän integroinnista tilitoimiston muihin järjestelmiin.
- **Tietoturva-asiantuntijat**: Varmistavat, että järjestelmä täyttää tietoturva- ja GDPR-vaatimukset.

---

### **2. Sidosryhmien analyysi (vaikutusvalta ja kiinnostus)**

| **Sidosryhmä**               | **Vaikutusvalta** | **Kiinnostus** | **Toimenpiteet**                                                                 |
|-------------------------------|-------------------|----------------|----------------------------------------------------------------------------------|
| Tilitoimiston johto           | Korkea           | Korkea         | Tiivis yhteistyö, säännölliset raportoinnit ja palautteen keruu.                |
| Tilitoimiston asiakkaat       | Matala           | Korkea         | Helppokäyttöinen sovellus, palautteen keruu ja käyttäjäkoulutus.                |
| IT-osasto                     | Korkea           | Matala         | Yhteistyö integraatioiden osalta, pidetään ajan tasalla.                        |
| Tietoturva-asiantuntijat      | Korkea           | Matala         | Tietoturvakatselmukset ja tietosuojakäytäntöjen noudattaminen.                  |
| Kehittäjät                    | Korkea           | Korkea         | Selkeät vaatimukset ja realistiset aikataulut.                                  |
| Tekoälyasiantuntijat          | Korkea           | Korkea         | Datan ja teknologian riittävän laadun varmistaminen.                            |
| UX-suunnittelijat             | Korkea           | Korkea         | Käyttäjätestaukset ja selkeä palautekanava loppukäyttäjiltä.                    |
| Testaajat                     | Korkea           | Korkea         | Testausprosessien suunnittelu ja jatkuva kommunikointi kehittäjien kanssa.      |

---

### **3. Visuaalinen stakeholder map**
Sidosryhmät voidaan sijoittaa **vaikutus-valta-matriisiin**, jossa korostetaan heidän merkitystään:

#### **Matriisi (Power-Interest Grid)**

1. **Korkea vaikutusvalta, korkea kiinnostus**:
   - Tilitoimiston johto
   - Kehittäjät
   - Tekoälyasiantuntijat
   - UX-suunnittelijat
   - Testaajat

2. **Korkea vaikutusvalta, matala kiinnostus**:
   - IT-osasto
   - Tietoturva-asiantuntijat


Sidosryhmä	                Vaikutusvalta	    Kiinnostus	    Toimenpiteet

Tilitoimiston johto	        Korkea	            Korkea	        Tiivis yhteistyö, säännölliset raportoinnit ja palautteen keruu.
Tilitoimiston asiakkaat 	Matala	            Korkea	        Helppokäyttöinen sovellus, palautteen keruu ja käyttäjäkoulutus.
IT-osasto	                Korkea	            Matala	        Yhteistyö integraatioiden osalta, pidetään ajan tasalla.
Tietoturva-asiantuntijat	Korkea	            Matala	        Tietoturvakatselmukset ja tietosuojakäytäntöjen noudattaminen.
Kehittäjät	                Korkea	            Korkea	        Selkeät vaatimukset ja realistiset aikataulut.
Tekoälyasiantuntijat	    Korkea	            Korkea	        Datan ja teknologian riittävän laadun varmistaminen.
UX-suunnittelijat	        Korkea	            Korkea	        Käyttäjätestaukset ja selkeä palautekanava loppukäyttäjiltä.
Testaajat	                Korkea	            Korkea	        Testausprosessien suunnittelu ja jatkuva kommunikointi kehittäjien kanssa.


3. **Matala vaikutusvalta, korkea kiinnostus**:
   - Tilitoimiston asiakkaat

4. **Matala vaikutusvalta, matala kiinnostus**:
   - Ei kriittisiä sidosryhmiä tässä kategoriassa.

---

### **4. Toimintasuunnitelma sidosryhmille**
- **Johdon sitouttaminen**: Säännölliset tilannekatsaukset ja päätöksenteon tukeminen.
- **Loppukäyttäjien huomioiminen**: Selkeä palautemekanismi ja käyttäjälähtöinen suunnittelu.
- **IT-osaston tuki**: Riittävä dokumentaatio ja tekninen apu integraatioihin.
- **Tietoturvan varmistaminen**: Säännölliset auditoinnit ja parhaiden käytäntöjen noudattaminen.

------

# Miten eri sidosryhmät haluavat järjestelmän toimivan?

Tässä ovat vastaukset esitettyihin kysymyksiin, pohjautuen tehtävänantoon ja MVP-lähestymistapaan:

---

### **1. Miten sovelluksen käyttäjä haluaisi puhelinsovelluksen toimivan?**
- **Helppokäyttöisyys:** Käyttäjät haluavat intuitiivisen sovelluksen, joka ei vaadi pitkiä oppimisprosessia. Toiminnot, kuten kuitin skannaaminen ja tietojen tarkistaminen, tulisi olla nopeita ja sujuvia.
- **Automaattisuus:** Sovelluksen tulisi tunnistaa kuitista tiedot automaattisesti ilman, että käyttäjä joutuu syöttämään niitä manuaalisesti.
- **Luotettavuus:** Käyttäjät odottavat, että sovellus tunnistaa oikein kuitin olennaiset tiedot (esim. summa, ALV, päivämäärä).
- **Integrointi:** Mahdollisuus viedä tiedot muihin järjestelmiin, kuten kirjanpito- tai raportointiohjelmiin.
- **Visuaalinen miellyttävyys:** Selkeä ja visuaalisesti miellyttävä käyttöliittymä, joka tekee prosessista miellyttävän.

---

### **2. Mitä tietoa yrityksen ylläpitäjä haluaisi järjestelmän tuottavan?**
- **Käyttöstatistiikka:**
  - Kuinka monta kuittia käyttäjät ovat käsitelleet kuukaudessa.
  - Keskimääräinen skannausten määrä per käyttäjä.
  - Käyttäjien aktiivisuus.
- **Virhetilastot:**
  - Kuinka monta kertaa kuitin tunnistus epäonnistui.
  - Yleisimmät ongelmakohdat (esim. epäselvä kuva, tuntemattomat kuitin rakenteet).
- **Sovellusversioiden seuranta:**
  - Tieto siitä, mitä sovellusversiota käyttäjät käyttävät.
  - Versiopäivitysten vaikutus.
- **Reaaliaikainen tilannekuva:** 
  - Järjestelmän käytön kuormitus ja mahdolliset häiriöt.
- **Käyttäjäpalautteet:** 
  - Mitä ongelmia käyttäjät raportoivat ja millaisia ominaisuuksia he toivovat.

---

### **3. Miten helppoa järjestelmän ylläpidon/kehityksen pitäisi olla?**
- **Modulaarisuus:** Järjestelmä tulisi rakentaa modulaarisesti, jotta uusia ominaisuuksia voidaan lisätä helposti ilman koko järjestelmän uudistamista.
- **Automaatiot:** Kehityksessä voidaan hyödyntää CI/CD-työkaluja (Continuous Integration/Continuous Deployment), jotka automatisoivat testauksen ja julkaisuprosessit.
- **Ketterä kehitys:** MVP-vaiheessa tärkeintä on nopeus ja joustavuus, mutta pitkässä juoksussa arkkitehtuurin tulisi mahdollistaa skaalautuvuus.
- **Helppo hallinta:** Ylläpidon pitäisi olla suoraviivaista, esimerkiksi käyttöliittymän asetusten ja analytiikan hallinnan tulisi olla intuitiivisia.

---

### **4. Mitä teknologioita voisi lähteä kokeilemaan?**
- **OCR (optinen merkintunnistus):** 
  - **Tesseract OCR** (ilmainen ja avoimen lähdekoodin ratkaisu).
  - **Google Vision API** (maksullinen, mutta tarjoaa tarkempia tuloksia ja helpon integraation).
- **Mobiilisovelluskehitys:**
  - **Flutter** (Googlelta, yksi koodipohja Androidille ja iOS:lle).
  - **React Native** (Facebookilta, tuki useille alustoille).
- **Pilvipalvelut:**
  - **Firebase** (reaaliaikainen tietokanta ja käyttäjähallinta).
  - **AWS Lambda** (serverless-ratkaisut, joissa maksat vain käytöstä).
- **Tietokannat:**
  - **PostgreSQL** (relaatiotietokanta monipuolisiin tarpeisiin).
  - **MongoDB** (dokumenttipohjainen tietokanta, helppo skaalata).
- **Analytiikka:**
  - **Google Analytics** käyttäjästatistiikkaan.
  - **Mixpanel** tai **Amplitude** käyttäjäpolkujen seurantaan.

---

### **5. Onko olemassa sovelluksia, joista voisi ottaa ideoita?**
- **Expensify:** Sovellus kulujen hallintaan, joka sisältää kuitin skannauksen ja automaattisen tiedonpoiminnan.
- **Wave Receipts:** Suunnattu pienyrityksille, sisältää kuitin tallennuksen ja integroinnin kirjanpitoon.
- **QuickBooks:** Kirjanpitosovellus, joka tukee kuitin skannausta ja tietojen analysointia.
- **SAP Concur:** Yritystason matkalaskujen ja kulukorvausten hallintasovellus.
- Näistä voidaan ottaa inspiraatiota erityisesti käyttäjäystävällisyyden, visuaalisen ilmeen ja automaation osalta.

---

### **6. Jatkokysymyksiä konseptoinnin tueksi**
- Mitä lisäarvoa järjestelmä voisi tuoda tilitoimistolle ja heidän asiakkailleen tulevaisuudessa?
- Pitäisikö sovellukseen lisätä kielituki, esimerkiksi englannille tai muille kielille?
- Kuinka tärkeää on real-time-analytiikka (esim. virheiden välitön raportointi)?
- Voisiko sovellus hyödyntää koneoppimista tunnistuksen parantamiseen?

Haluatko, että laajennan jotain näistä kohdista tai teen konkreettisen toimintasuunnitelman?