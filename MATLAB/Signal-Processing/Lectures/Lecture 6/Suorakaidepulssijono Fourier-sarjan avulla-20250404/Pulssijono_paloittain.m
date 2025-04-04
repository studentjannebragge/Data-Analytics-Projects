clear
% Määritellään suorakaidepulssijonon parametrit
A=2;
d=0.5;
T=2;
% Muodostetaan aikavektori
t=-5:0.01:5;
% Muodostetaan DC-komponentti
DC=A*d/T;
% Alustetaan taajuuskomponenttien lukumäärä
lkm1=10;
% Alustetaan signaali
signaali_taulukko=zeros([lkm1,length(t)]);
% Muodostetaan DC-signaali
DC_signaali=zeros(1,length(t))+DC;
plot(t,DC_signaali)
legend('DC-komponentti')
xlabel('AIKA')
ylabel('SIGNAALIN ARVO')
waitforbuttonpress
% Luodaan signaalin 10 ensimmäistä taajuuskomponenttia for-silmukassa ja
% tallennetaan signaalit taulukkoon
for k=1:lkm1
    signaali_taulukko(k,:)=2*A/k/pi*sin(k*pi*d/T)*cos(k*2*pi*t/T);
    plot(t, signaali_taulukko(k,:))
    teksti=['Signaalin ',num2str(k),'.','taajuuskomponentti',', jonka taajuus = ',num2str((1/T)*k),' Hz'];
    title(teksti)
    xlabel('AIKA')
    ylabel('SIGNAALIN ARVO')
    waitforbuttonpress
end

% Piirretään kaikki signaalit samaan ikkunaan
figure;
plot(t,DC_signaali)
hold on
for k=1:lkm1
    plot(t, signaali_taulukko(k,:))
end
xlabel('AIKA')
ylabel('SIGNAALIN ARVO')
title('DC-komponentti ja 10.ensimmäistä taajuuskomponenttia')
hold off
waitforbuttonpress


figure;
% Muodostetaan summasignaali
Summasignaali=DC_signaali+sum(signaali_taulukko,1);
plot(t,Summasignaali)
xlabel('AIKA')
ylabel('SIGNAALIN ARVO')
title('DC-komponentti ja 10.ensimmäistä taajuuskomponenttia summattuna')
waitforbuttonpress

lkm2=100;
signaali_taulukko=zeros([lkm2,length(t)]);

for k=1:lkm2
    signaali_taulukko(k,:)=2*A/k/pi*sin(k*pi*d/T)*cos(k*2*pi*t/T);
   % plot(t, signaali_taulukko(k,:))
    %teksti=['Signaalin ',num2str(k),'.','taajuuskomponentti',', jonka taajuus = ',num2str((1/T)*k),' Hz'];
    %title(teksti)
    %xlabel('AIKA')
    %ylabel('SIGNAALIN ARVO')
    %waitforbuttonpress
end

figure;
% Muodostetaan summasignaali
Summasignaali=DC_signaali+sum(signaali_taulukko,1);
plot(t,Summasignaali)
xlabel('AIKA')
ylabel('SIGNAALIN ARVO')
title('DC-komponentti ja 100.ensimmäistä taajuuskomponenttia summattuna')

waitforbuttonpress

lkm3=1000;
signaali_taulukko=zeros([lkm3,length(t)]);

for k=1:lkm3
    signaali_taulukko(k,:)=2*A/k/pi*sin(k*pi*d/T)*cos(k*2*pi*t/T);
   % plot(t, signaali_taulukko(k,:))
    %teksti=['Signaalin ',num2str(k),'.','taajuuskomponentti',', jonka taajuus = ',num2str((1/T)*k),' Hz'];
    %title(teksti)
    %xlabel('AIKA')
    %ylabel('SIGNAALIN ARVO')
    %waitforbuttonpress
end

figure;
% Muodostetaan summasignaali
Summasignaali=DC_signaali+sum(signaali_taulukko,1);
plot(t,Summasignaali)
xlabel('AIKA')
ylabel('SIGNAALIN ARVO')
title('DC-komponentti ja 1000.ensimmäistä taajuuskomponenttia summattuna')
ylim([-0.2 2.2])
waitforbuttonpress

lkm4=10000;
signaali_taulukko=zeros([lkm4,length(t)]);


for k=1:lkm4
    signaali_taulukko(k,:)=2*A/k/pi*sin(k*pi*d/T)*cos(k*2*pi*t/T);
   % plot(t, signaali_taulukko(k,:))
    %teksti=['Signaalin ',num2str(k),'.','taajuuskomponentti',', jonka taajuus = ',num2str((1/T)*k),' Hz'];
    %title(teksti)
    %xlabel('AIKA')
    %ylabel('SIGNAALIN ARVO')
    %waitforbuttonpress
end

figure;
% Muodostetaan summasignaali
Summasignaali=DC_signaali+sum(signaali_taulukko,1);
plot(t,Summasignaali)
xlabel('AIKA')
ylabel('SIGNAALIN ARVO')
title('DC-komponentti ja 10000.ensimmäistä taajuuskomponenttia summattuna')
ylim([-0.2 2.2])


waitforbuttonpress

close all

%{

subplot(3,1,1)
plot(t, signaali)
% Alustetaan signaali
signaali=zeros([1,length(t)]);
% Lisätään DC-komponentti signaaliin
signaali=signaali+DC;
% Alustetaan taajuuskomponenttien lukumäärä
lkm2=10;
% Lisätään signaaliin for-silmukassa taajuuskomponetteja
for k=1:lkm2
    signaali=signaali+2*A/k/pi*sin(k*pi*d/T)*cos(k*2*pi*t/T);
end
subplot(3,1,2)
plot(t, signaali)
% Alustetaan signaali
signaali=zeros([1,length(t)]);
% Lisätään DC-komponentti signaaliin
signaali=signaali+DC;
% Alustetaan taajuuskomponenttien lukumäärä
lkm3=100;
% Lisätään signaaliin for-silmukassa taajuuskomponetteja
for k=1:lkm3
    signaali=signaali+2*A/k/pi*sin(k*pi*d/T)*cos(k*2*pi*t/T);
end
subplot(3,1,3)
plot(t, signaali)

%}
