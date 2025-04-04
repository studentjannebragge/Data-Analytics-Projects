Tässä ohje Excelin **loogisten funktioiden** käytöstä! Loogiset funktiot ovat hyödyllisiä päätöksentekoon ja ehdollisiin laskelmiin, kuten "jos tämä, niin tuo" -skenaarioiden käsittelyyn.

---

## 📜 **Yleiskatsaus Excelin loogisiin funktioihin**

Loogiset funktiot palauttavat tyypillisesti **TRUE** (tosi) tai **FALSE** (epätosi) riippuen annetuista ehdoista. Näitä voidaan yhdistää muiden funktioiden kanssa.

---

### 🧩 **1. Perusloogiset funktiot**
#### **IF**
- **Kuvaus**: Tarkistaa ehdon ja palauttaa arvon sen perusteella, onko ehto tosi tai epätosi.
- **Kaava**: `=IF(logical_test, value_if_true, value_if_false)`
- **Esimerkki**:
  - `=IF(A1>10, "Suuri", "Pieni")`  
  - Jos solun A1 arvo on yli 10, tulos on "Suuri", muuten "Pieni".

---

#### **AND**
- **Kuvaus**: Tarkistaa, ovatko kaikki ehdot totta.
- **Kaava**: `=AND(logical1, [logical2], ...)`
- **Esimerkki**:
  - `=AND(A1>10, B1<20)`  
  - Palauttaa **TRUE**, jos A1 on suurempi kuin 10 **ja** B1 on pienempi kuin 20.

---

#### **OR**
- **Kuvaus**: Tarkistaa, onko jokin annetuista ehdoista tosi.
- **Kaava**: `=OR(logical1, [logical2], ...)`
- **Esimerkki**:
  - `=OR(A1>10, B1<20)`  
  - Palauttaa **TRUE**, jos **jompikumpi** ehdoista on tosi.

---

#### **NOT**
- **Kuvaus**: Kääntää ehdon loogisen arvon.
- **Kaava**: `=NOT(logical)`
- **Esimerkki**:
  - `=NOT(A1>10)`  
  - Palauttaa **TRUE**, jos A1 ei ole suurempi kuin 10.

---

### 🧮 **2. Ehdollisten tilanteiden funktiot**
#### **IFERROR**
- **Kuvaus**: Palauttaa määritetyn arvon, jos kaava aiheuttaa virheen.
- **Kaava**: `=IFERROR(value, value_if_error)`
- **Esimerkki**:
  - `=IFERROR(A1/B1, "Virhe")`  
  - Palauttaa A1/B1 tuloksen, jos lasku onnistuu, mutta palauttaa "Virhe", jos B1 on nolla.

---

#### **IFS**
- **Kuvaus**: Tarkistaa useita ehtoja ja palauttaa ensimmäisen toden arvon mukaisen tuloksen.
- **Kaava**: `=IFS(logical_test1, value_if_true1, [logical_test2, value_if_true2], ...)`
- **Esimerkki**:
  - `=IFS(A1>10, "Suuri", A1>5, "Keskikokoinen", A1<=5, "Pieni")`  
  - Tarkistaa A1:n arvon ja palauttaa tuloksen sen mukaan.

---

#### **SWITCH**
- **Kuvaus**: Valitsee tuloksen useista vaihtoehdoista.
- **Kaava**: `=SWITCH(expression, value1, result1, [value2, result2], ..., default)`
- **Esimerkki**:
  - `=SWITCH(A1, 1, "Yksi", 2, "Kaksi", "Muu")`  
  - Jos A1 on 1, palauttaa "Yksi"; jos 2, palauttaa "Kaksi"; muuten "Muu".

---

### 🔍 **3. Tosi- ja epätosi-tuloksia hyödyntävät funktiot**
#### **TRUE**
- **Kuvaus**: Palauttaa aina **TRUE**.
- **Kaava**: `=TRUE()`
- **Esimerkki**:
  - Voidaan käyttää ehdollisessa tarkastelussa.

#### **FALSE**
- **Kuvaus**: Palauttaa aina **FALSE**.
- **Kaava**: `=FALSE()`
- **Esimerkki**:
  - Voidaan käyttää ehdollisessa tarkastelussa.

#### **XOR**
- **Kuvaus**: Palauttaa **TRUE**, jos vain yksi ehdoista on tosi.
- **Kaava**: `=XOR(logical1, [logical2], ...)`
- **Esimerkki**:
  - `=XOR(A1>10, B1<20)`  
  - Palauttaa **TRUE**, jos **vain yksi** ehdoista on tosi.

---

### 🎯 **Esimerkki yhdistetyistä loogisista funktioista**
#### **Useiden ehtojen tarkastelu**
- **Kaava**:  
  `=IF(AND(A1>10, OR(B1="Kyllä", C1="Ei")), "Hyväksytty", "Hylätty")`
- **Selitys**:
  - Jos A1 on suurempi kuin 10 ja joko B1 on "Kyllä" **tai** C1 on "Ei", tulos on "Hyväksytty". Muuten tulos on "Hylätty".

---

## 📊 **Käyttöesimerkkejä taulukossa**

| **Kaava**                           | **Tulos**       |
|-------------------------------------|-----------------|
| `=IF(A1>10, "Kyllä", "Ei")`         | "Kyllä" (jos A1 > 10) |
| `=AND(A1>10, B1<20)`                | TRUE            |
| `=OR(A1>10, B1<20)`                 | TRUE            |
| `=NOT(A1>10)`                       | FALSE (jos A1 > 10) |
| `=IFERROR(A1/B1, "Virhe")`          | "Virhe" (jos B1 = 0) |
| `=IFS(A1>10, "Suuri", A1>5, "Keskikokoinen", A1<=5, "Pieni")` | Riippuu A1:n arvosta |

---

