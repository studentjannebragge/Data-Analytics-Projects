function DFT_x = DFT_vektoreilla (x)
%Funktio saa syötteenään reaalisen signaalin vaakavektorina
%Funktio muodostaa signaalille DFT:n määritelmän mukaisesti
%Paluuarvoina ovat DFT:n komponentit muuttujassa DFT_x

%Tutkitaan signaalin pituus
N=length(x);


%Muodostetaan taulukko (matriisi) DFT:n eksponentiaaliosalle exp(-1i*2*pi*k*n/N)

%Luodaan nollataulukko
eksp_osat=zeros(N,N);

%Luodaan taulukko, johon tallennetaan kaikki kombinaatiot operaatiolle k*n.
%Sarakkeet edustavat k:n arvoja, rivit n:n arvoja
eksp_osat=[0:1:N-1]' * [0:1:N-1]

%Sijoitetaan yllä luotu taulukko DFT:n eksponettiosan lausekkeeseen
%Tuloksena saadaan kaikki kombinaatiot halutuille k:n ja n:n arvoille
eksp_osat=exp(-1i*2*pi*eksp_osat/N);

%Kerrotaan vaakavektori x taulukon [N x N] kanssa. Tuloksena saadaan DFT.
DFT_x=x*eksp_osat;

disp('Oman funktion tulos')
DFT_x

disp('Octaven funktion tulos')
fft(x)



endfunction

