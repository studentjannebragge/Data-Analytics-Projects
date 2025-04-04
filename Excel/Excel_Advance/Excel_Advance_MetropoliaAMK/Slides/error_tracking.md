Tässä ovat ohjeet Excelin **virheiden jäljittämisestä**, jotta voit helposti löytää ja korjata laskentataulukossasi esiintyvät virheet.

---

## 📜 **Yleiskatsaus**

Excelissä virheitä voi esiintyä esimerkiksi kaavoissa, viittauksissa tai tietosyötössä. Virheiden jäljittämiseen on useita työkaluja ja tekniikoita, jotka auttavat löytämään ongelman lähteen ja korjaamaan sen.

---

### 🔎 **1. Yleisimmät virhekoodit**
| **Virhekoodi** | **Selitys**                                  | **Ratkaisu**                           |
|----------------|----------------------------------------------|----------------------------------------|
| `#DIV/0!`     | Jakaminen nollalla tai tyhjällä solulla.     | Varmista, ettei jakaja ole 0 tai tyhjä. |
| `#VALUE!`     | Kaava käyttää väärän tyyppistä dataa.         | Tarkista kaavassa käytettyjen solujen arvot. |
| `#REF!`       | Viitataan poistettuun tai olemattomaan soluun.| Korjaa kaavaviittaukset.               |
| `#NAME?`      | Excel ei tunnista käytettyä nimeä tai kaavaa. | Tarkista, että kaavan nimi on oikein.  |
| `#N/A`        | Arvoa ei löydy hausta.                       | Tarkista hakufunktioiden tiedot.       |
| `#NULL!`      | Kahden alueen välillä ei ole leikkauspistettä.| Varmista, että alueet on yhdistetty oikein. |

---

### 🛠️ **2. Virheiden jäljittämisen työkalut**

#### **Kaavan tarkastustyökalut**
1. **Avaa Data-välilehti**:
   - Siirry **Formulas**- (Kaavat) tai **Data**-välilehteen.
2. **Error Checking** (Virheentarkistus):
   - Valitse **Error Checking** -painike.
   - Tämä tarkistaa kaikki virheet taulukossa ja antaa ohjeita korjaamiseen.

---

#### **Esikatselu solussa**
- Klikkaa virheellistä solua.
- Näet kaavan **kaavarivillä**. Tarkista, onko kaavassa viittausongelmia, kuten tyhjiä soluja, väärä kaava tai poistetut solut.

---

#### **Trace Precedents** (Edeltäjät)
- **Kuvaus**: Näyttää, mistä solut tai kaavat saavat arvonsa.
- **Miten käyttää**:
  1. Valitse solu, jossa on virhe.
  2. Klikkaa **Formulas**-välilehdeltä **Trace Precedents**.
  3. Nuolikaavio näyttää solut, joista nykyinen kaava riippuu.

---

#### **Trace Dependents** (Riippuvuudet)
- **Kuvaus**: Näyttää, mitkä solut käyttävät valitun solun arvoa.
- **Miten käyttää**:
  1. Valitse solu.
  2. Klikkaa **Trace Dependents** nähdäksesi, missä muualla tätä solua käytetään.

---

#### **Evaluate Formula** (Kaavan arviointi)
- **Kuvaus**: Näyttää kaavan osittaisen arvioinnin vaihe vaiheelta.
- **Miten käyttää**:
  1. Valitse solu, jossa on kaava.
  2. Klikkaa **Formulas**-välilehdeltä **Evaluate Formula**.
  3. Seuraa askel askeleelta, miten Excel laskee kaavan.

---

#### **Remove Arrows** (Poista nuolet)
- **Kuvaus**: Poistaa kaaviot ja nuolet jäljitystyökalujen käytön jälkeen.
- **Miten käyttää**:
  1. Siirry **Formulas**-välilehdelle.
  2. Valitse **Remove Arrows**, jos haluat selkeyttää näkymän.

---

### 🔧 **3. Kaavan ja datan tarkistaminen**
#### **Show Formulas** (Näytä kaavat)
- **Kuvaus**: Näyttää solujen laskenta-arvojen sijaan itse kaavat.
- **Miten käyttää**:
  1. Paina **Ctrl + `** (näppäin löytyy Esc:n alapuolelta).
  2. Kaikki kaavat näkyvät nyt taulukossa.

---

#### **Find and Replace** (Etsi ja korvaa)
- **Kuvaus**: Etsi solut, joissa on tietty kaava, viittaus tai virhe.
- **Miten käyttää**:
  1. Paina **Ctrl + F**.
  2. Kirjoita hakukenttään esim. `#REF!`.
  3. Klikkaa **Find All** nähdäksesi kaikki esiintymät.

---

#### **Error Indicators** (Virheiden merkit)
- **Kuvaus**: Soluissa, joissa on virheitä, näkyy vihreä kolmio solun kulmassa.
- **Miten käyttää**:
  1. Klikkaa solua, jossa on vihreä kolmio.
  2. Klikkaa varoitusikonia saadaksesi ehdotuksia korjaukselle.

---

### ✨ **4. Käytännön vinkkejä virheiden korjaamiseen**
- **Käytä IFERROR**:
  - **Kuvaus**: Korvaa kaavan tuottama virhe mukautetulla arvolla.
  - **Kaava**: `=IFERROR(kaava, "Virheviesti")`
  - **Esimerkki**:  
    `=IFERROR(A1/B1, "Jakovirhe")`  
    - Palauttaa "Jakovirhe", jos B1 on nolla.
    
- **Käytä tarkistustoimintoja**:
  - **Data Validation**: Aseta sääntöjä syötetylle datalle (esim. "vain numerot").
  - **Conditional Formatting**: Korosta virhesolut automaattisesti.

---

### 🎯 **Esimerkki käytännössä**

| **Solu** | **Kaava**        | **Tulos**        | **Ratkaisu**                  |
|----------|------------------|------------------|-------------------------------|
| A1       | `=B1/C1`         | `#DIV/0!`        | Käytä `=IFERROR(B1/C1, "Virhe")` |
| B1       | `=D1+E1`         | `#REF!`          | Korjaa poistettu viittaus.    |
| C1       | `=VLOOKUP(101, A1:B10, 3, FALSE)` | `#N/A` | Tarkista hakutaulukon tiedot. |

---
