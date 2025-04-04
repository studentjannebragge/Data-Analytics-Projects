Tässä ovat Excelin **Financial**-funktiot selityksineen ja esimerkkikäyttöineen! Nämä funktiot ovat erityisen hyödyllisiä talousanalyysissä, kuten lainojen, investointien ja kassavirtojen laskemisessa.

---

### 💰 **1. LASKUT TALOUDELLISISTA KASSAVIRROISTA**
#### **NPV (Net Present Value)**
- **Kuvaus**: Laskee investoinnin nykyarvon diskonttaamalla tulevat kassavirrat.
- **Kaava**: `=NPV(rate, value1, [value2], ...)`
- **Käyttö**: Investointien kannattavuuden arviointi.
- **Esimerkki**: `=NPV(5%, A1:A10)`

#### **XNPV**
- **Kuvaus**: Laskee nykyarvon, kun kassavirrat eivät ole tasavälein.
- **Kaava**: `=XNPV(rate, cash_flows, dates)`
- **Käyttö**: Epäsäännöllisten maksujen analysointiin.

#### **IRR (Internal Rate of Return)**
- **Kuvaus**: Laskee projektin sisäisen tuottoprosentin.
- **Kaava**: `=IRR(values, [guess])`
- **Käyttö**: Investointien tuottavuuden analysointiin.
- **Esimerkki**: `=IRR(A1:A10)`

#### **XIRR**
- **Kuvaus**: Laskee sisäisen korkokannan epäsäännöllisille maksuille.
- **Kaava**: `=XIRR(cash_flows, dates, [guess])`
- **Käyttö**: Kassavirtojen ajoituksen huomioiva tuottoanalyysi.

---

### 💵 **2. LASKUT KORKOKUSTANNUKSISTA JA LAINOISTA**
#### **PMT (Payment)**
- **Kuvaus**: Laskee lainan kuukausierän annuiteettimenetelmällä.
- **Kaava**: `=PMT(rate, nper, pv, [fv], [type])`
- **Käyttö**: Lainojen kuukausierien laskemiseen.
- **Esimerkki**: `=PMT(5%/12, 60, -10000)`

#### **IPMT (Interest Payment)**
- **Kuvaus**: Laskee lainan koron tietylle kuukaudelle.
- **Kaava**: `=IPMT(rate, per, nper, pv, [fv], [type])`
- **Käyttö**: Korkokulujen erittely lainan keston aikana.

#### **PPMT (Principal Payment)**
- **Kuvaus**: Laskee lyhennyksen lainan pääomasta tietylle kuukaudelle.
- **Kaava**: `=PPMT(rate, per, nper, pv, [fv], [type])`
- **Käyttö**: Pääoman lyhennyksen tarkasteluun.

#### **CUMIPMT**
- **Kuvaus**: Laskee lainan kokonaiskorot tietyltä ajanjaksolta.
- **Kaava**: `=CUMIPMT(rate, nper, pv, start_period, end_period, type)`
- **Käyttö**: Kokonaiskorkojen analysointi.

#### **CUMPRINC**
- **Kuvaus**: Laskee lainan kokonaispääoman lyhennyksen tietyltä ajanjaksolta.
- **Kaava**: `=CUMPRINC(rate, nper, pv, start_period, end_period, type)`
- **Käyttö**: Pääoman lyhennyksen erittely.

---

### 📈 **3. ARVON MÄÄRITTÄMINEN**
#### **PV (Present Value)**
- **Kuvaus**: Laskee investoinnin nykyarvon.
- **Kaava**: `=PV(rate, nper, pmt, [fv], [type])`
- **Käyttö**: Tulevien kassavirtojen arvon määrittely.
- **Esimerkki**: `=PV(5%/12, 60, -200)`

#### **FV (Future Value)**
- **Kuvaus**: Laskee tulevan arvon, kun tiedetään maksut ja korko.
- **Kaava**: `=FV(rate, nper, pmt, [pv], [type])`
- **Käyttö**: Sijoitusten tulevan arvon arviointi.

#### **RATE**
- **Kuvaus**: Laskee korkokannan tietylle aikavälille.
- **Kaava**: `=RATE(nper, pmt, pv, [fv], [type], [guess])`
- **Käyttö**: Apu korkoprosentin määrittämiseen.
- **Esimerkki**: `=RATE(60, -200, -10000)`

#### **NPER**
- **Kuvaus**: Laskee maksukertojen määrän lainalle.
- **Kaava**: `=NPER(rate, pmt, pv, [fv], [type])`
- **Käyttö**: Apu maksuohjelman suunnitteluun.

---

### 🔍 **4. LISÄTYÖKALUT TALOUDELLISEEN ANALYYSIIN**
#### **SLN (Straight Line Depreciation)**
- **Kuvaus**: Laskee tasapoiston omaisuudelle.
- **Kaava**: `=SLN(cost, salvage, life)`
- **Käyttö**: Poistoarvon laskemiseen yksinkertaisilla menetelmillä.

#### **DB (Declining Balance Depreciation)**
- **Kuvaus**: Laskee vähenevän saldon poistot.
- **Kaava**: `=DB(cost, salvage, life, period, [month])`
- **Käyttö**: Nopeamman poistotahdin määrittämiseen.

#### **SYD (Sum-of-Years’ Digits Depreciation)**
- **Kuvaus**: Laskee poistot sum-of-years-menetelmällä.
- **Kaava**: `=SYD(cost, salvage, life, period)`
- **Käyttö**: Arvon alenemisen laskeminen tasaisesti.

#### **DDB (Double Declining Balance Depreciation)**
- **Kuvaus**: Laskee kaksinkertaisella menetelmällä tapahtuvat poistot.
- **Kaava**: `=DDB(cost, salvage, life, period, [factor])`
- **Käyttö**: Omaisuuden poiston nopea aikataulu.

---
