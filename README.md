# eKool
eKool realisatsioon, kasutades selleks OOP printsiipe. Projektile on kirjutatud ka testid, mis kontrollivad erinevaid olukordi.

#Projekti nõuded
Projektis tuleks realiseerida vähemalt järgnev:
* koolis toimuvad ained,
* õpilasel on nimi, klass ja keskmine hinne,
* õpilane saab kooli registreeruda,
* õpilane saab korraga olla vaid ühes koolis,
* aine on seotud kooliga, sellel on nimi, õpetaja(d) ja õpetatav(ad) klass(id),
* ühte ainet võib sooritada mitu klassi (näiteks matemaatika 1. - 12. klass),
* ühte ainet võib õpetada mitu õpetajat,
* üks õpetaja võib õpetada mitut ainet,
* üks õpetaja võib õpetada mitmes koolis,
* õpilane saab ainele registreeruda (seda ainult juhul kui ta on antud kooli registreerunud),
* õpilane saab aine sooritada või läbi kukkuda,
* kui õpilane sooritab aine, siis ta saab selle eest hinde,
* hinded on 1, 2, 3, 4, 5,
* kui õpilane saab aine eest hindeks 1 või 2, on ta aine läbi kukkunud,
* õpilasel on ülevaade sooritatud (ja mitte sooritatud) ainetest,
* koolil on ülevaade õpilasest, ainetest ja õpetajatest,
* koolil on võimalik moodustada õpilaste pingerida keskmise hinde alusel.

# Piirangute kontroll
Projektis tuleks kontrollida mõistlikkuse piires erinevaid piiranguid, näiteks:
* õpilase klass peaks olema vahemikus 1-12,
* õpilase keskmine hinne peaks olema vahemikus 1-5,
* sisestatud hinne ei saa olla väljaspool määratud vahemikku,
* õpilane ei ole korraga rohkem kui ühes koolis,
* õpilast ei saa registreerida kursusele, kui seda tema klassile ei õpetata jne.

# Programmi testimine
Programmi testimiseks võiks proovida näiteks sellist sündmuste ahelat:
```luuakse uus kool
luuakse hulk õpetajaid
luuakse hulk õpilasi
õpilased lisatakse kooli
luuakse teine kool
kontrollitakse, et üks õpilane ei saa mitmes koolis olla
kooli luuakse erinevad ained
proovitakse luua vigaseid aineid
õpilane registreeritakse ainele
õpilane saab aine sooritatud
õpilane kukub aine läbi
õpilane näeb enda hinnete ajalugu
koolist saab vaadata õpilaste nimekirja
koolist saab vaadata õpetajate nimekirja
koolist saab vaadata ainete nimekirja
õpetaja näeb enda õpetatavaid aineid
kool väljastab õpilaste pingerea nende keskmise hinde põhjal
```
kool väljastab õpilaste pingerea nende keskmise hinde põhjal
# Meeskond
* Anna Karutina - [anna.karutina@voco.ee](mailto:anna.karutina@vocom.ee) - Projektijuht, arendaja
* Mihhail Karutin - [mihhail.karutin@voco.ee](mailto:mihhail.karutin@vocom.ee) - Arendaja, testija
