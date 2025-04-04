% Laskostumisen tutkiminen

clear

close all

f=input('Syötä sinisignaalin taajuus [Hz] positiivisena kokonaislukuna: ');

fs=input('Syötä signaalin näytteistystaajuus [Hz] positiivisena kokonaislukuna: ');

% Lasketaan Nyqvistin taajuus
f_nyq=fs/2;

% Tulostetaan lähtötiedot
disp(['Signaalin taajuus on: ', num2str(f), ' Hz']);

disp(['Signaalin näytteistystaajuus on: ', num2str(fs), 'Hz'])

disp(['Nyquistin taajuus on: ', num2str(f_nyq), 'Hz'])


% Tutkitaan, onko näytteistystaajuus riittävä laskostumisen estämiseksi

if fs < (2*f)
    disp('Näytteistystaajuus on liian alhainen, signaali laskostuu!')
    end

% Luodaan aikavektori, joka täyttää Nyquistin ehdon. Näytteet otetaan 100
% kertaisella taajuudella  näytteistettävän signaalin taajuuteen verrattuna
dt1=1/(f*100);
t1=0:dt1:5-dt1; % Signaalin pituus = 5 s - dt1

% Muodostetaan signaali, jonka näytepisteiden välinen etäisyys on dt1
signaali1=sin(2*pi*f*t1);

% Piirretään signaali
plot(t1,signaali1)
xlabel('AIKA')
ylabel('SIGNAALIN ARVO')
hold on

% Luodaan aikavektori, jonka aikainkrementti määräytyy fs:n perusteella
dt2=1/fs;
t2=0:dt2:5-dt2;

% Muodostetaan signaali, jonka näytteiden väli aikatasossa määräytyy fs:n
% perusteella
signaali2=sin(2*pi*f*t2);
%Piirretään signaali samaan kuvaan signaali1:en kanssa
plot(t2,signaali2,'r')
hold off










