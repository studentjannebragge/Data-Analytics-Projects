function [sign] = IDFT_algoritmi( X )
  %Funktio saa syötteenään DFT:n komponentit ja muodostaa niiden perusteella aikatason signaalin
  %Funktio palauttaa IDFT:n avulla muodostetun signaalin

%Tutkitaan DFT:n pituus ja alustetaan signaalille taulukko
N=length(X);
sign=zeros(1,N);

%Suoritetaan IDFT:n muodostaminen sisäkkäisillä silmukoilla
for n= 0 : N-1 %Muistettava määritelmän mukainen indeksointi
for k= 0 : N-1

sign(n+1)=sign(n+1)+X(k+1)*exp(1i*2*pi*k*n/N); %muodostetaan signaali kumulatiivisesti summaamalla

end
end
%Joskus signaaliin jää pyöristysvirheiden takia mukaan olemattoman pieniä imaginaariosia
%Seuraavassa ne poistetaan real-komennolla sekä suoritetaan kaikkien komponenttien jakaminen N:llä määritelmän mukaisesti
sign=real(sign)/N;

%esitetään signaali
stem(sign)

end

