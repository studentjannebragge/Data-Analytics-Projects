Tässä ohjeet Excelin **hakufunktioista**. Hakufunktiot ovat erityisen hyödyllisiä tietojen etsimisessä ja yhdistämisessä taulukoiden välillä.

---

## 📜 **Yleiskatsaus Excelin hakufunktioihin**

Excelin hakufunktiot auttavat etsimään arvoja taulukosta tai määritetystä alueesta nopeasti ja tehokkaasti.

---

### 🧩 **1. Yleiset hakufunktiot**
#### **VLOOKUP** (Pystysuuntainen haku)
- **Kuvaus**: Hakee arvon taulukon ensimmäiseltä sarakkeelta ja palauttaa saman rivin tiedon toisesta sarakkeesta.
- **Kaava**: `=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])`
  - **lookup_value**: Arvo, jota etsitään.
  - **table_array**: Taulukkoalue, josta arvo etsitään.
  - **col_index_num**: Palautettavan sarakkeen numero.
  - **range_lookup**: **TRUE** (likimääräinen vastaavuus) tai **FALSE** (täsmällinen vastaavuus).
- **Esimerkki**:
  - `=VLOOKUP(101, A1:C10, 2, FALSE)`  
  - Etsii arvon 101 ensimmäisestä sarakkeesta ja palauttaa toisen sarakkeen tiedon.

---

#### **HLOOKUP** (Vaakasuuntainen haku)
- **Kuvaus**: Hakee arvon taulukon ensimmäiseltä riviltä ja palauttaa saman sarakkeen tiedon toiselta riviltä.
- **Kaava**: `=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])`
- **Esimerkki**:
  - `=HLOOKUP("Otsikko", A1:Z2, 2, FALSE)`  
  - Etsii arvon "Otsikko" ensimmäiseltä riviltä ja palauttaa tiedon toiselta riviltä.

---

#### **XLOOKUP** (Monipuolinen haku)
- **Kuvaus**: Etsii arvon määritetyltä alueelta ja palauttaa vastaavan arvon toiselta alueelta. Tukee pystysuuntaista, vaakasuuntaista ja dynaamista hakua.
- **Kaava**: `=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`
- **Esimerkki**:
  - `=XLOOKUP(101, A1:A10, B1:B10, "Ei löydy")`  
  - Etsii arvon 101 alueelta A1:A10 ja palauttaa vastaavan arvon alueelta B1:B10.

---

### 🔄 **2. Hakeminen indeksien ja viitteiden avulla**
#### **INDEX**
- **Kuvaus**: Palauttaa arvon tietystä rivistä ja sarakkeesta alueella.
- **Kaava**: `=INDEX(array, row_num, [column_num])`
- **Esimerkki**:
  - `=INDEX(A1:C10, 2, 3)`  
  - Palauttaa arvon toiselta riviltä ja kolmannesta sarakkeesta alueella A1:C10.

---

#### **MATCH**
- **Kuvaus**: Palauttaa haettavan arvon sijainnin alueessa.
- **Kaava**: `=MATCH(lookup_value, lookup_array, [match_type])`
  - **match_type**: 
    - **1** = likimääräinen arvo, nousevassa järjestyksessä.
    - **0** = täsmällinen arvo.
    - **-1** = likimääräinen arvo, laskevassa järjestyksessä.
- **Esimerkki**:
  - `=MATCH(50, A1:A10, 0)`  
  - Palauttaa arvon 50 sijainnin alueella A1:A10.

---

#### **INDEX + MATCH**
- **Kuvaus**: Yhdistää INDEX- ja MATCH-funktiot joustavampaan hakuun.
- **Kaava**:  
  `=INDEX(return_array, MATCH(lookup_value, lookup_array, 0))`
- **Esimerkki**:
  - `=INDEX(B1:B10, MATCH(101, A1:A10, 0))`  
  - Etsii arvon 101 alueelta A1:A10 ja palauttaa vastaavan arvon alueelta B1:B10.

---

### 🔍 **3. Hakutoiminnot tietojen analysointiin**
#### **LOOKUP**
- **Kuvaus**: Hakee arvon yhdeltä riviltä tai sarakkeelta ja palauttaa toisen rivin tai sarakkeen arvon.
- **Kaava**: `=LOOKUP(lookup_value, lookup_vector, [result_vector])`
- **Esimerkki**:
  - `=LOOKUP(50, A1:A10, B1:B10)`  
  - Etsii arvon 50 alueelta A1:A10 ja palauttaa vastaavan arvon alueelta B1:B10.

---

#### **FILTER**
- **Kuvaus**: Suodattaa alueen tiettyjen ehtojen perusteella.
- **Kaava**: `=FILTER(array, include, [if_empty])`
- **Esimerkki**:
  - `=FILTER(A1:C10, A1:A10>100, "Ei tuloksia")`  
  - Suodattaa alueen A1:C10 palauttaen vain rivit, joiden ensimmäinen sarake on yli 100.

---

#### **UNIQUE**
- **Kuvaus**: Palauttaa luettelosta ainutlaatuiset arvot.
- **Kaava**: `=UNIQUE(array, [by_col], [exactly_once])`
- **Esimerkki**:
  - `=UNIQUE(A1:A10)`  
  - Palauttaa alueen A1:A10 ainutlaatuiset arvot.

---

### 🎯 **Käyttöesimerkkejä taulukossa**

| **Funktio**               | **Kaava**                      | **Tulos**                  |
|----------------------------|--------------------------------|----------------------------|
| Pystysuuntainen haku       | `=VLOOKUP(101, A1:C10, 2, FALSE)` | Löytää 101:n rivin arvon. |
| Dynaaminen haku            | `=XLOOKUP(101, A1:A10, B1:B10)`   | Palauttaa arvon B1:B10:stä. |
| Suodattaminen             | `=FILTER(A1:C10, A1:A10>50)`    | Palauttaa rivit, joissa A1 > 50. |
| Ainutlaatuiset arvot        | `=UNIQUE(A1:A10)`             | Palauttaa ainutlaatuiset arvot. |

---
