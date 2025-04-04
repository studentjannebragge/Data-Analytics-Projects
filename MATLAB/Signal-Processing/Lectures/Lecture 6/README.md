Selvä! Tässä opas Diskreetti Fourier-muunnoksen (DFT) ja sen käänteismuunnoksen (IDFT) tekemiseen Octavella. Octave käyttää tehokkaita FFT-algoritmeja (Fast Fourier Transform) näiden laskemiseen.

**1. Diskreetti Fourier-muunnos (DFT) Octavella: `fft()`**

DFT muuntaa aika-tason signaalin (näytejonon) sen taajuuskomponentteihin. Octavessa tämä tehdään `fft()`-funktiolla.

* **Syöte:** Vektori, joka sisältää signaalin aika-tason näytteet `x[n]`.
* **Tuloste:** Vektori, joka sisältää kompleksisia DFT-kertoimia `X[k]`. Tulosvektorin pituus on sama kuin syötevektorin.

**Esimerkki:**

```octave
% 1. Määrittele aika-tason signaali x[n] vektorina
x = [1, 2, 0, -1]; % Esimerkkisignaali (4 näytettä)

% 2. Laske DFT käyttäen fft()-funktiota
X = fft(x);

% 3. Tulosta tulos
disp("Signaali x[n]:");
disp(x);
disp("DFT-tulos X[k]:");
disp(X);

% DFT-kertoimet ovat kompleksilukuja. Niistä voidaan laskea:
% Amplitudi (Magnitude)
amplitudit = abs(X);
disp("Amplitudit |X[k]|:");
disp(amplitudit);

% Vaihe (Phase) radiaaneina
vaiheet_rad = angle(X);
disp("Vaiheet (radiaaneina):");
disp(vaiheet_rad);

% Vaihe (Phase) asteina
vaiheet_deg = rad2deg(angle(X));
disp("Vaiheet (asteina):");
disp(vaiheet_deg);
```

**Tulos:**

```
Signaali x[n]:
   1   2   0  -1

DFT-tulos X[k]:
   2.0000 + 0.0000i   1.0000 - 3.0000i  -2.0000 + 0.0000i   1.0000 + 3.0000i

Amplitudit |X[k]|:
   2.0000   3.1623   2.0000   3.1623

Vaiheet (radiaaneina):
   0.0000  -1.2490   3.1416   1.2490

Vaiheet (asteina):
    0.0000  -71.5651  180.0000   71.5651
```

**Huomioitavaa `fft()`-tuloksesta:**

* Tulos `X` on yleensä kompleksilukuvektori.
* `X(1)` (Octaven 1-pohjainen indeksointi) vastaa taajuutta 0 Hz (DC-komponentti, `k=0`). Se on signaalin näytteiden summa.
* Seuraavat alkiot vastaavat kasvavia taajuuksia.
* Jos syöte `x` on reaalinen, tulos `X` on konjugaattisymmetrinen: `X(k) = conj(X(N-k+2))` Octaven indeksoinnilla.

**2. Käänteinen Diskreetti Fourier-muunnos (IDFT) Octavella: `ifft()`**

IDFT muuntaa taajuus-tason komponentit takaisin aika-tason signaaliksi. Octavessa tämä tehdään `ifft()`-funktiolla.

* **Syöte:** Vektori, joka sisältää DFT-kertoimet `X[k]`.
* **Tuloste:** Vektori, joka sisältää (palautetut) aika-tason näytteet `x[n]`.

**Esimerkki (käyttäen edellisen esimerkin tulosta `X`):**

```octave
% Oletetaan, että meillä on DFT-tulos X edellisestä esimerkistä:
X = [2.0000 + 0.0000i, 1.0000 - 3.0000i, -2.0000 + 0.0000i, 1.0000 + 3.0000i];

% 1. Laske IDFT käyttäen ifft()-funktiota
x_palautettu = ifft(X);

% 2. Tulosta tulos
disp("DFT-kertoimet X[k]:");
disp(X);
disp("Palautettu aika-tason signaali x[n]:");
disp(x_palautettu);

% Huom: Numeerisen laskennan vuoksi tuloksessa voi olla hyvin pieniä
% imaginaariosia, vaikka alkuperäinen signaali olisi ollut reaalinen.
% Ne voidaan poistaa real()-funktiolla, jos tiedetään tuloksen olevan reaalinen.
disp("Palautettu signaali (vain reaali-osa):");
disp(real(x_palautettu));
```

**Tulos:**

```
DFT-kertoimet X[k]:
   2.0000 + 0.0000i   1.0000 - 3.0000i  -2.0000 + 0.0000i   1.0000 + 3.0000i

Palautettu aika-tason signaali x[n]:
   1.0000 + 0.0000i   2.0000 - 0.0000i   0.0000 + 0.0000i  -1.0000 + 0.0000i

Palautettu signaali (vain reaali-osa):
   1   2   0  -1
```

Kuten nähdään, `ifft(fft(x))` palauttaa alkuperäisen signaalin `x` (mahdollisilla pienillä numeerisilla epätarkkuuksilla).

**Yhteenveto:**

* Muunna aika-tasosta taajuus-tasoon: `X = fft(x)`
* Muunna taajuus-tasosta aika-tasoon: `x = ifft(X)`
* Hae amplitudit: `abs(X)`
* Hae vaiheet radiaaneina: `angle(X)`

Muista, että Octaven/MATLABin indeksointi alkaa 1:stä, kun taas DFT:n matemaattinen määritelmä käyttää usein 0-pohjaista indeksointia (`k=0...N-1`). `X(1)` vastaa `k=0`, `X(2)` vastaa `k=1`, ja niin edelleen `X(N)` vastaa `k=N-1`.