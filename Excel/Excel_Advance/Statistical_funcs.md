Excelin **statistiset funktiot** tarjoavat laajan valikoiman työkaluja tilastolliseen analyysiin. Alla on selitykset ja käyttötarkoitukset kaikille Excelin *Statistical*-funktioihin kuuluville funktioille:

---

### 📊 **1. PERUSTILASTOT**
#### **AVERAGE**
- **Kuvaus**: Laskee valitun alueen keskiarvon.
- **Kaava**: `=AVERAGE(A1:A10)`
- **Käyttö**: Sopii esimerkiksi opiskelijoiden keskiarvon laskemiseen.

#### **MEDIAN**
- **Kuvaus**: Palauttaa lukujoukon mediaanin.
- **Kaava**: `=MEDIAN(A1:A10)`
- **Käyttö**: Keskiluvun määrittäminen, kun halutaan poistaa ääriarvojen vaikutus.

#### **MODE.SNGL**
- **Kuvaus**: Palauttaa joukossa yleisimmin esiintyvän arvon.
- **Kaava**: `=MODE.SNGL(A1:A10)`
- **Käyttö**: Esimerkiksi asiakaskäyttäytymisen analysointiin.

#### **MODE.MULT**
- **Kuvaus**: Palauttaa kaikki joukossa useimmin esiintyvät arvot.
- **Kaava**: `=MODE.MULT(A1:A10)`
- **Käyttö**: Hyödyllinen silloin, kun on useita usein toistuvia arvoja.

#### **STDEV.P** / **STDEV.S**
- **Kuvaus**: Laskee populaation (P) tai otoksen (S) keskihajonnan.
- **Kaava**: `=STDEV.P(A1:A10)`
- **Käyttö**: Datan hajonnan mittaamiseen.

#### **VAR.P** / **VAR.S**
- **Kuvaus**: Laskee populaation (P) tai otoksen (S) varianssin.
- **Kaava**: `=VAR.P(A1:A10)`
- **Käyttö**: Datan hajonnan mittaamiseen keskihajonnan rinnalla.

---

### 📈 **2. JAKAUMIEN ANALYYSI**
#### **NORM.DIST**
- **Kuvaus**: Laskee normaalijakauman todennäköisyydet.
- **Kaava**: `=NORM.DIST(x, mean, standard_dev, cumulative)`
- **Käyttö**: Analysoimaan normaalijakauman mukaisia tietoja.

#### **NORM.INV**
- **Kuvaus**: Palauttaa normaalijakauman käänteisen arvon.
- **Kaava**: `=NORM.INV(probability, mean, standard_dev)`
- **Käyttö**: Tietyn persentiilin arvon laskemiseen.

#### **POISSON.DIST**
- **Kuvaus**: Laskee Poisson-jakauman.
- **Kaava**: `=POISSON.DIST(x, mean, cumulative)`
- **Käyttö**: Tapahtumien ennustaminen tietyllä aikavälillä.

#### **T.DIST**
- **Kuvaus**: Laskee t-jakauman todennäköisyydet.
- **Kaava**: `=T.DIST(x, deg_freedom, cumulative)`
- **Käyttö**: T-testien tulosten analysointiin.

---

### 🧮 **3. TODENNÄKÖISYYDET JA KORRELAATIOT**
#### **PROB**
- **Kuvaus**: Laskee tapahtuman todennäköisyyden tietyssä välissä.
- **Kaava**: `=PROB(range, prob_range, lower_limit, upper_limit)`
- **Käyttö**: Todennäköisyyden arviointi.

#### **CORREL**
- **Kuvaus**: Laskee kahden tietojoukon välisen korrelaation.
- **Kaava**: `=CORREL(array1, array2)`
- **Käyttö**: Esimerkiksi myynnin ja markkinoinnin välisen suhteen arviointiin.

#### **COVARIANCE.P** / **COVARIANCE.S**
- **Kuvaus**: Laskee populaation tai otoksen kovarianssin.
- **Kaava**: `=COVARIANCE.P(array1, array2)`
- **Käyttö**: Muuttujien välisten suhteiden analysointi.

---

### 📌 **4. ERIKOISLASKENTAA**
#### **FREQUENCY**
- **Kuvaus**: Laskee tietojoukon esiintymistiheydet.
- **Kaava**: `=FREQUENCY(data_array, bins_array)`
- **Käyttö**: Esimerkiksi tenttipisteiden luokitteluun.

#### **COUNTIF**
- **Kuvaus**: Laskee soluja, jotka täyttävät tietyt ehdot.
- **Kaava**: `=COUNTIF(range, criteria)`
- **Käyttö**: Tiettyjen arvojen esiintymien laskeminen.

#### **RANK.EQ** / **RANK.AVG**
- **Kuvaus**: Palauttaa arvon sijainnin joukossa.
- **Kaava**: `=RANK.EQ(number, ref, order)`
- **Käyttö**: Tietyn tuloksen sijoittaminen suhteessa muihin.

---

### ✨ **5. SATUNNAISLUVUT**
#### **RAND**
- **Kuvaus**: Luo satunnaisluvun välillä 0 ja 1.
- **Kaava**: `=RAND()`
- **Käyttö**: Simulointien luomiseen.

#### **RANDBETWEEN**
- **Kuvaus**: Luo satunnaisluvun annetulta väliltä.
- **Kaava**: `=RANDBETWEEN(bottom, top)`
- **Käyttö**: Esimerkiksi arvontojen luomiseen.

---
