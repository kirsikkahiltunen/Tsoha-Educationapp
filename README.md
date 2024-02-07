# Opetussovellus
Sovelluksen aihe on yksi tietokannat ja web ohjelmointi kurssin esimerkki aiheista. Sovellus on tarkoitettu verkkokurssien järjestämistä vrten tietokannat ja web ohjelmointi kurssin sivuilla esitellyn mukaisesti:

Sovelluksen avulla voidaan järjestää verkkokursseja, joissa on tekstimateriaalia ja automaattisesti tarkastettavia tehtäviä. Jokainen käyttäjä on opettaja tai opiskelija.

Sovelluksen ominaisuuksia:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Opiskelija näkee listan kursseista ja voi liittyä kurssille.
- Opiskelija voi lukea kurssin tekstimateriaalia sekä ratkoa kurssin tehtäviä.
- Opiskelija pystyy näkemään tilaston, mitkä kurssin tehtävät hän on ratkonut.
- Opettaja pystyy luomaan uuden kurssin, muuttamaan olemassa olevaa kurssia ja poistamaan kurssin.
- Opettaja pystyy lisäämään kurssille tekstimateriaalia ja tehtäviä. Tehtävä voi olla ainakin monivalinta tai tekstikenttä, johon tulee kirjoittaa oikea vastaus.
- Opettaja pystyy näkemään kurssistaan tilaston, keitä opiskelijoita on kurssilla ja mitkä kurssin tehtävät kukin on ratkonut.


Ohjelman perusominaisuudet kuten sisäänkirjautuminen ja käyttäjätunnuksen rekisteröiminen on luonnosteltu. Kuitenkin suurinosa sovelluksen toiminnoista on vielä työn alla, einkä ole esimerkiksi saanut tietokantaa toimimaan. 


Pääset testaamaan sovellusta kopioimalla tämän repositorion omalle koneellesi.


Aja sitten seuraavat käskyt:


$ python3 -m venv venv


$ source venv/bin/activate


$ flask run


Etusivulta pääset kirjautumis tai rekisteröitymissivulle. Voit halutessasi kokeilla kirjautumista eri statuksilla, navigoimalla ensin kirjautumissivulle ja sitten kirjautumalla käyttäjänimellä demo_oppilas ja salasanalla demo_oppilas, jotta pääset opiskelijalle tarkoitetulle "kurssit sivulle", kirjautumalla käyttäjänimellä demo_opettaja ja salasanalla demo_opettaja, pääset vastaavasti tarkastelemaan opettajan kurssi sivua. Kurssisivun toimintoja ei ole vielä rakennettu. 




