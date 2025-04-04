Tässä kattavat ohjeet Excelin **pyöristysfunktioista**. Näitä funktioita käytetään numeroiden pyöristämiseen tiettyyn tarkkuuteen, kuten kokonaislukuihin, desimaaleihin tai tiettyihin kerrannaisiin.

---

## 📐 **1. Yleiset pyöristysfunktiot**
### **ROUND**
- **Kuvaus**: Pyöristää luvun lähimpään haluttuun desimaaliin.
- **Kaava**: `=ROUND(number, num_digits)`
  - **number**: Pyöristettävä luku.
  - **num_digits**: Desimaalien määrä (positiivinen = desimaali, 0 = kokonaisluku, negatiivinen = kymmenet/sataset).
- **Esimerkki**:
  - `=ROUND(123.456, 2)` palauttaa **123.46**.
  - `=ROUND(123.456, -1)` palauttaa **120**.

---

### **ROUNDUP**
- **Kuvaus**: Pyöristää luvun ylöspäin (poispäin nollasta) haluttuun tarkkuuteen.
- **Kaava**: `=ROUNDUP(number, num_digits)`
- **Esimerkki**:
  - `=ROUNDUP(123.456, 2)` palauttaa **123.46**.
  - `=ROUNDUP(123.456, -1)` palauttaa **130**.

---

### **ROUNDDOWN**
- **Kuvaus**: Pyöristää luvun alaspäin (kohti nollaa) haluttuun tarkkuuteen.
- **Kaava**: `=ROUNDDOWN(number, num_digits)`
- **Esimerkki**:
  - `=ROUNDDOWN(123.456, 2)` palauttaa **123.45**.
  - `=ROUNDDOWN(123.456, -1)` palauttaa **120**.

---

## 🔢 **2. Kokonaislukujen pyöristys**
### **INT**
- **Kuvaus**: Palauttaa luvun kokonaisosan (pyöristää alaspäin lähimpään kokonaislukuun).
- **Kaava**: `=INT(number)`
- **Esimerkki**:
  - `=INT(123.456)` palauttaa **123**.
  - `=INT(-123.456)` palauttaa **-124**.

---

### **TRUNC**
- **Kuvaus**: Katkaisee luvun haluttuun desimaalien määrään (ei pyöristystä).
- **Kaava**: `=TRUNC(number, [num_digits])`
  - **num_digits** (valinnainen): Haluttu desimaalien määrä.
- **Esimerkki**:
  - `=TRUNC(123.456, 2)` palauttaa **123.45**.
  - `=TRUNC(-123.456)` palauttaa **-123**.

---

### **CEILING**
- **Kuvaus**: Pyöristää luvun ylöspäin lähimpään kerrannaiseen.
- **Kaava**: `=CEILING(number, significance)`
  - **significance**: Kerrannainen, johon pyöristetään.
- **Esimerkki**:
  - `=CEILING(123.456, 0.1)` palauttaa **123.5**.
  - `=CEILING(-123.456, 10)` palauttaa **-120**.

---

### **FLOOR**
- **Kuvaus**: Pyöristää luvun alaspäin lähimpään kerrannaiseen.
- **Kaava**: `=FLOOR(number, significance)`
- **Esimerkki**:
  - `=FLOOR(123.456, 0.1)` palauttaa **123.4**.
  - `=FLOOR(-123.456, 10)` palauttaa **-130**.

---

### **MROUND**
- **Kuvaus**: Pyöristää luvun lähimpään kerrannaiseen.
- **Kaava**: `=MROUND(number, multiple)`
  - **multiple**: Luku, jonka kerrannaiseen pyöristetään.
- **Esimerkki**:
  - `=MROUND(123.456, 0.5)` palauttaa **123.5**.
  - `=MROUND(123.456, 10)` palauttaa **120**.

---

## 💡 **3. Erikoisfunktiot**
### **EVEN**
- **Kuvaus**: Pyöristää luvun ylöspäin lähimpään parilliseen kokonaislukuun.
- **Kaava**: `=EVEN(number)`
- **Esimerkki**:
  - `=EVEN(123.456)` palauttaa **124**.
  - `=EVEN(-123.456)` palauttaa **-124**.

---

### **ODD**
- **Kuvaus**: Pyöristää luvun ylöspäin lähimpään parittomaan kokonaislukuun.
- **Kaava**: `=ODD(number)`
- **Esimerkki**:
  - `=ODD(123.456)` palauttaa **125**.
  - `=ODD(-123.456)` palauttaa **-125**.

---

## 🎯 **Käyttöesimerkkejä**

| **Funktio**       | **Kaava**             | **Tulos** |
|--------------------|-----------------------|-----------|
| ROUND              | `=ROUND(12.3456, 2)` | 12.35     |
| ROUNDUP            | `=ROUNDUP(12.3456, 2)` | 12.35     |
| ROUNDDOWN          | `=ROUNDDOWN(12.3456, 2)` | 12.34 |
| INT                | `=INT(12.3456)`      | 12        |
| TRUNC              | `=TRUNC(12.3456, 2)` | 12.34     |
| CEILING            | `=CEILING(12.3456, 0.1)` | 12.4 |
| FLOOR              | `=FLOOR(12.3456, 0.1)` | 12.3 |
| MROUND             | `=MROUND(12.3456, 0.1)` | 12.3 |

---

