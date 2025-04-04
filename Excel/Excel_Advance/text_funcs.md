Tässä ovat ohjeet Excelin **tekstifunktioista**, joiden avulla voit käsitellä ja muotoilla tekstidataa tehokkaasti!

---

## 📜 **Yleiskatsaus Excelin tekstifunktioihin**

Excelin tekstifunktiot sopivat erinomaisesti, kun haluat esimerkiksi erotella, yhdistellä tai muokata tekstimuotoista dataa taulukoissasi.

---

### 🧩 **1. Tekstin yhdistäminen ja muokkaaminen**
#### **TEXTJOIN**
- **Kuvaus**: Yhdistää tekstiarvot määritetyllä erotinmerkillä, ja voit ohittaa tyhjät arvot.
- **Kaava**: `=TEXTJOIN(delimiter, ignore_empty, text1, [text2], ...)`
- **Esimerkki**:
  - `=TEXTJOIN(", ", TRUE, A1:A3)`  
  - Yhdistää solut A1–A3 pilkulla eroteltuina.

---

#### **CONCAT**
- **Kuvaus**: Yhdistää tekstiarvot ilman erotinta.
- **Kaava**: `=CONCAT(text1, [text2], ...)`
- **Esimerkki**:
  - `=CONCAT(A1, B1, " ", C1)`  
  - Yhdistää solut A1, B1 ja C1, lisäten välilyönnin niiden väliin.

---

#### **& (Ampersand-operaattori)**
- **Kuvaus**: Yhdistää tekstiarvot nopeasti.
- **Kaava**: `=A1 & " " & B1`
- **Esimerkki**:
  - `="Hei, " & A1`  
  - Yhdistää "Hei, " ja solun A1 sisällön.

---

#### **LEFT**
- **Kuvaus**: Palauttaa tekstin alusta tietyn merkkimäärän.
- **Kaava**: `=LEFT(text, num_chars)`
- **Esimerkki**:
  - `=LEFT(A1, 5)`  
  - Palauttaa solun A1 ensimmäiset 5 merkkiä.

---

#### **RIGHT**
- **Kuvaus**: Palauttaa tekstin lopusta tietyn merkkimäärän.
- **Kaava**: `=RIGHT(text, num_chars)`
- **Esimerkki**:
  - `=RIGHT(A1, 3)`  
  - Palauttaa solun A1 kolme viimeistä merkkiä.

---

#### **MID**
- **Kuvaus**: Palauttaa tekstistä tietyn osan, alkaen määritetystä kohdasta.
- **Kaava**: `=MID(text, start_num, num_chars)`
- **Esimerkki**:
  - `=MID(A1, 3, 5)`  
  - Palauttaa solun A1 kolmannesta merkistä alkaen 5 merkkiä.

---

### 🔤 **2. Tekstin muotoilu**
#### **UPPER**
- **Kuvaus**: Muuttaa tekstin isoiksi kirjaimiksi.
- **Kaava**: `=UPPER(text)`
- **Esimerkki**:
  - `=UPPER(A1)`  
  - Muuttaa solun A1 sisällön isoiksi kirjaimiksi.

---

#### **LOWER**
- **Kuvaus**: Muuttaa tekstin pieniksi kirjaimiksi.
- **Kaava**: `=LOWER(text)`
- **Esimerkki**:
  - `=LOWER(A1)`  
  - Muuttaa solun A1 sisällön pieniksi kirjaimiksi.

---

#### **PROPER**
- **Kuvaus**: Muuttaa tekstin niin, että jokainen sana alkaa isolla kirjaimella.
- **Kaava**: `=PROPER(text)`
- **Esimerkki**:
  - `=PROPER(A1)`  
  - Muuttaa "esimerkki teksti" muotoon "Esimerkki Teksti".

---

#### **TEXT**
- **Kuvaus**: Muotoilee numerot tai päivämäärät tekstiksi tietyn kaavan mukaan.
- **Kaava**: `=TEXT(value, format_text)`
- **Esimerkki**:
  - `=TEXT(A1, "dd.mm.yyyy")`  
  - Muuntaa päivämäärän muotoon "20.12.2024".

---

### 🔍 **3. Tekstin analysointi ja muokkaaminen**
#### **LEN**
- **Kuvaus**: Laskee tekstin merkkimäärän (sisältää välilyönnit).
- **Kaava**: `=LEN(text)`
- **Esimerkki**:
  - `=LEN(A1)`  
  - Laskee solun A1 tekstin pituuden.

---

#### **FIND**
- **Kuvaus**: Palauttaa määritetyn tekstin sijainnin toisessa tekstissä (isoilla ja pienillä kirjaimilla on merkitystä).
- **Kaava**: `=FIND(find_text, within_text, [start_num])`
- **Esimerkki**:
  - `=FIND("k", A1)`  
  - Palauttaa ensimmäisen "k"-kirjaimen sijainnin A1:ssä.

---

#### **SEARCH**
- **Kuvaus**: Kuten FIND, mutta ei erottele isoja ja pieniä kirjaimia.
- **Kaava**: `=SEARCH(find_text, within_text, [start_num])`
- **Esimerkki**:
  - `=SEARCH("teksti", A1)`  
  - Palauttaa "teksti"-sanan sijainnin.

---

#### **TRIM**
- **Kuvaus**: Poistaa tekstin alusta, lopusta ja keskeltä ylimääräiset välilyönnit (paitsi yksittäiset välit sanojen välillä).
- **Kaava**: `=TRIM(text)`
- **Esimerkki**:
  - `=TRIM(A1)`  
  - Poistaa ylimääräiset välilyönnit solusta A1.

---

#### **CLEAN**
- **Kuvaus**: Poistaa tekstistä tulostamattomat merkit.
- **Kaava**: `=CLEAN(text)`
- **Esimerkki**:
  - `=CLEAN(A1)`  
  - Poistaa tulostamattomat merkit A1:stä.

---

### ✨ **4. Tekstin korvaaminen**
#### **SUBSTITUTE**
- **Kuvaus**: Korvaa määritetyn osan tekstistä toisella tekstillä.
- **Kaava**: `=SUBSTITUTE(text, old_text, new_text, [instance_num])`
- **Esimerkki**:
  - `=SUBSTITUTE(A1, "vanha", "uusi")`  
  - Korvaa "vanha" sanalla "uusi" solussa A1.

---

#### **REPLACE**
- **Kuvaus**: Korvaa tekstin tietyn osan määritetystä kohdasta alkaen.
- **Kaava**: `=REPLACE(old_text, start_num, num_chars, new_text)`
- **Esimerkki**:
  - `=REPLACE(A1, 3, 5, "XYZ")`  
  - Korvaa A1:n kolmannesta merkistä alkaen viisi merkkiä "XYZ":llä.

---

### 🎯 **Käyttöesimerkkejä taulukossa**

| **Funktio**              | **Kaava**                      | **Tulos**                 |
|---------------------------|--------------------------------|---------------------------|
| Yhdistäminen              | `=TEXTJOIN(", ", TRUE, A1:A3)`| "A1, A2, A3"              |
| Isot kirjaimet            | `=UPPER("esimerkki")`         | "ESIMERKKI"               |
| Pienet kirjaimet          | `=LOWER("ESIMERKKI")`         | "esimerkki"               |
| Korvaaminen               | `=SUBSTITUTE("vanha teksti", "vanha", "uusi")` | "uusi teksti" |

---

