%Signaalin uudelleennäytteistäminen (resample)

%Resample-komennolla digitaalinen signaali voidaan turvallisesta näyteistää uudelleen
%Komento pitää huolen siitä, ettei laskostumista tapahdu
%HOX! Näytepisteiden pudottaminen signaalista huolettomasti voisi johtaa laskostumiseen
% [y, h] = resample (x, p, q)
% https://octave.sourceforge.io/signal/function/resample.html


%LUODAAN TESTISIGNAALI

pkg load signal
pkg load control

fs=100; %N�ytteistystaajuus
dt=1/fs; %Aikainkrementti

t=(0:1:(fs*2-1))*dt; %2 sekunnin mittainen aikavektori

k1=cos(2*pi*2*t); %Kosinisignaali, taajuus 2 Hz
k2=2*cos(2*pi*7*t); %Kosinisignaali, taajuus 7 Hz
k3=3*cos(2*pi*13*t); %Kosinisignaali, taajuus 13 Hz

k_yhd=[k1 k2 k3]; %Liitet��n signaalit per�kk�in

t_yhd=(0:1:(length(k_yhd)-1))*dt; % luodaan aikavektori yhdistelm�signaalille

kohina=0.1*randn(1,length(k_yhd)); %Luodaan kohinasgnaali

test_sig=k_yhd+kohina; % Summataan kosinisignaaliin kohinaa

%Esitet��n testisignaali graafisesti
plot(t_yhd,test_sig)
xlabel('Aika [s]')
ylabel('Signaalin arvo')
grid on
title('Testisignaali')

waitforbuttonpress

%LASKETAAN SIGNAALIN N�YTTEISTYSTAAJUUTTA FUNKTIOLLA "RESAMPLE"


new_fs=20; %Uusi n�ytteistystaajuus

test_sig_res=resample(test_sig,new_fs,fs); %N�ytteistet��n signaali uudestaan
t_res=(0:1:length(test_sig_res)-1)*(1/new_fs); %Luodaan signaalille uusi aikavektori


%Esitet��n uudelleen n�ytteistetty signaali aikatasossa
figure;
plot(t_res,test_sig_res)
xlabel('Aika [s]')
ylabel('Signaalin arvo')
title('Resampled signal, Fs=20 Hz')
grid on

waitforbuttonpress

%NÄYTTEISTETÄÄN EM. SIGNAALI YLÖSPÄIN ALKUPERÄISEEN NÄYTTEISTYSTAAJUUTEEN 100 Hz

test_sig_res_up=resample(test_sig_res,100,20); %N�ytteistet��n signaali uudestaan ylöspäin
t_res=(0:1:length(test_sig_res_up)-1)*(1/100); %Luodaan signaalille uusi aikavektori

figure;
plot(t_res,test_sig_res_up)
xlabel('Aika [s]')
ylabel('Signaalin arvo')
title('Upsampled signal, Fs=100 Hz')
grid on

waitforbuttonpress
%HUOMIO! Resample-komentoa voi käyttää myös (ideaalisena) alipäästösuodattimena
%Signaalin voi aluksi näytteistää alaspain ja sitten takaisin ylöspäin
%Resample-komento on hyödyllinen myös datamäärän vähentämisessä
%Läheskään aina ei tarvita koko taajuusaluetta


close all



