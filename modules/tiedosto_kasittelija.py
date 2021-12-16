# tiedosto_kasittelija on tiedostojen käsittelyyn tehty moduuli.
# Sen funktioilla voidaan arvotut lottonumerot tallentaa tiedostoon
# ja lukea tiedostosta.
#
# TODO: lauantaipyhien huomioon ottaminen virallisen arvonnan
# päivätestissä siten, että viikko tulee poikkeuksissa oikein.
#
# TODO: Päivämäärätarkastelun siirtäminen omaan moduuliinsa.


from os import strerror
from datetime import date, datetime, timedelta
import csv, datetime


def lue_lottonumerot():
    try:
        tiedosto = open('numerot/arvotut_lotto.txt', 'rt')
        print(tiedosto.read())
        tiedosto.close()

    except IOError as e:
        print("tapahtui IO virhe: ", strerror(e.errno))


def tallenna_lottonumerot(numerot):
    try:
        # Luetaan virallisen lottoarvonnan aika tiedostosta.
        tiedosto_lottoaika = open ('lottoarvonta-aika.txt', 'rt')
        aika_tiedoston_luku = csv.reader(tiedosto_lottoaika, delimiter = ":")

        arvonta_tunti = []

        for row in aika_tiedoston_luku:
            for element in row:
                arvonta_tunti.append(element)
            
        tiedosto_lottoaika.close()

        # Lasketaan montako sekuntia puolestayöstä virallinen arvonta on lauantaina.
        sekunnitArvontaTunti = 3600 * int(arvonta_tunti[0]) + 60 * int(arvonta_tunti[1])
        
        # Otetaan aikaleima arvontahetkelle, jolloin lottorivit arvotaan ohjelmalla.
        arvontaHetki = datetime.datetime.now()

        # Lasketaan sekunnit arvontahetkelle puolestayöstä.
        sekunnitArvontaHetki = 3600 * int(arvontaHetki.strftime("%H")) + 60 * int(arvontaHetki.strftime("%M"))

        # Otetaan arvontahetken isokalenteri leima, josta saadaan viikonnumero.
        isokalenteri = date.isocalendar(date.today())

        # Tarkastetaan onko viikonpäivä alle 5 (ma-pe 0-4).
        if arvontaHetki.weekday() < 5:
            vuosi_viikko = str(isokalenteri[0]) + "," + str(isokalenteri[1]) + ","

        # Tarkistetaan onko sunnuntai (6).
        elif arvontaHetki.weekday() > 5:
            # Jos sunnuntai, lisätään yksi päivä, jotta saadaan seuraava maanantai ja
            # näin ollen seuraava viikko.
            isokalenteri = date.isocalendar(date.today() + datetime.timedelta(days=1))
            vuosi_viikko = str(isokalenteri[0]) + "," + str(isokalenteri[1]) + ","
        else:
            # Jos ei ole viikon päivä pienempi kuin 5 tai isompi kuin 5, se on 5
            # eli lauantai. Tarkistetaan kellonaika.
            # Jos kello vähemmän kuin arvonta-aika, niin kirjataan käsillä olevalle viikolle.
            if sekunnitArvontaHetki < sekunnitArvontaTunti:
                vuosi_viikko = str(isokalenteri[0]) + "," + str(isokalenteri[1]) + ","

            # Muuten ohjelman arvonta-aika ylittänyt virallisen arvonta-ajan.
            # On lauantai, joten lisätään 2 päivää, jotta seuraavan viikon maanantai.
            else:
                isokalenteri = date.isocalendar(date.today() + datetime.timedelta(days=2))
                vuosi_viikko = str(isokalenteri[0]) + "," + str(isokalenteri[1]) + ","


        tiedosto = open('numerot/arvotut_lotto.txt', 'at')

        for listaelementti in numerot:

            pilkkulaskuri2 = len(listaelementti)
            tiedosto.write(vuosi_viikko)
            for rivi in listaelementti:
                
                pilkkulaskuri = len(rivi)

                for number in rivi:
                    num = str(number)

                    if pilkkulaskuri > 1:
                        num +=  ","
                    pilkkulaskuri -= 1

                    tiedosto.write(num)
                
                if pilkkulaskuri2 > 1:
                    tiedosto.write(",")
                pilkkulaskuri2 -= 1
                
            tiedosto.write("\n")

        tiedosto.close()

    except IOError as e:
        print("tapahtui IO virhe: ", strerror(e.errno))



# moduulin testaus

if __name__ == "__main__":
    try:
        testirivi = [([1,2,3,4,5,6,7],[8])]
        tallenna_lottonumerot(testirivi)

    except IOError as e:
        print("jotain tapahtui", strerror(e.errno))
    

    try:
        lue_lottonumerot()

    except IOError as e:
        print("jotain tapahtui", strerror(e.errno))

    # Testataan launtaisiirtymää.
    isokalenteri = date.isocalendar(date.today() + datetime.timedelta(days=4))
    vuosi_viikko = str(isokalenteri[0]) + "," + str(isokalenteri[1]) + ","
    print (isokalenteri)
    print (vuosi_viikko)

    # Testataan sekunttivertailua:
    tiedosto_lottoaika = open ('lottoarvonta-aika.txt', 'rt')
    aika_tiedoston_luku = csv.reader(tiedosto_lottoaika, delimiter = ":")

    arvonta_tunti = []

    for row in aika_tiedoston_luku:
        for element in row:
            arvonta_tunti.append(element)
                
    tiedosto_lottoaika.close()
    sekunnitArvontaTunti = 3600 * int(arvonta_tunti[0]) + 60 * int(arvonta_tunti[1])
    arvontaHetki = datetime.datetime.now()
    sekunnitArvontaHetki = 3600 * int(arvontaHetki.strftime("%H")) + 60 * int(arvontaHetki.strftime("%M"))
    print (sekunnitArvontaHetki < sekunnitArvontaTunti)