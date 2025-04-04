function [ DFT_x ] = DFT_algoritmi( x )
% Funktio laskee syötteenä saadun diskreettiaikaisen aikatason signaalin x
% diskreetin Fourier-muunnoksen (DFT=taajuustason esitys signaalista)

%Määritetään signaalin pituus
N=length(x);

% Muodostetaan DFT-komponenteille vektori, jonka pituus on N ja joka on alustettu nollilla
%DFT_x=zeros(1,N);

%{
 Lasketaan DFT-komponentit silmukassa
for k= 0 : N-1
for n= 0 : N-1
    % Lasketaan kukin DFT-komponentti kumulatiivisesti summaamalla kaikilla
    % n:n arvoilla saatavat välitulokset keskenään
DFT_x(k+1)=DFT_x(k+1)+x(n+1)*exp(-1i*2*pi*k*n/N);
end
end
%}

%Toinen vaihtoehto
DFT_x=zeros(N,N); %Taulukon alustus nollilla

for k= 0 : N-1
for n= 0 : N-1

%Muodostetaan arvoista taulukko siten, että kullekin k:n arvolle lasketut
%komponentit sijoitetaan omille sarakkeilleen. Taulukon koko on täten (k x n),
%kutakin k:n arvoa vastaavat komponentit sijoitetaan omille
%sarakkeilleen taulukkoon. Tämä on sama periaate kuin laskuharjoituksissa.
DFT_x(k+1,n+1)= x(n+1)*exp(-1i*2*pi*k*n/N);






%DFT_x(k+1,n+1)=x(n+1)*exp(-1i*2*pi*k*n/N);

end
end

%Summataan kullakin rivillä olevat arvot keskenään
DFT_x=sum(DFT_x,2);
%Käännetään syntynyt pystyvektori vaakavektoriksi (tässä yhteydessä
%transpoosikomento on piste+heittomerkki (.'), muutoin komento muodostaa
%samalla kompleksikonjugaatin.
DFT_x=DFT_x.';



