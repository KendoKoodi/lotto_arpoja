# Kokoava_loppuharjoitus, tehnyt Mika Virtala AVTAS19 Karelia-AMK SmartICT täydennyskoulutus.
#
# Ohjelma arpoo lottorivin ja lisänumerot ja tallentaa sen tiedostoon csv-muotoon (comma separated values).
#
# Lottoarpominen on toteutettu "arpakone" -luokalla, joka mahdollistaa saman luokan
# käytön myös muihin lottotyyppeihin kuin 7 numeroa 40:stä tyyppiseen.
#
# Tiedoston käsittely on eriytetty omaksi moduulikseen.


from sys import path

path.append('\\modules')

import modules.lottoarpoja as lottoarpoja
import modules.tiedosto_kasittelija as tiedosto

# Luodaan arpakone.
arpakone = lottoarpoja.arpakone()

print("Montako sekoitusta haluat pallojen välillä (kokonaisluku, oletus 4, max 100)?: ")
luuppimuuttuja = False
while not luuppimuuttuja:

    try:
        sekoituksetLukija = input()

        if sekoituksetLukija == '':
            sekoitukset = 4
        else:
            sekoitukset = int(sekoituksetLukija)

        if sekoitukset > 0 and sekoitukset < 101:
            luuppimuuttuja = True
        else:
            print("luku ulkona 1-100 arvoväliltä")

    except ValueError:
        print("syötetty arvo ei ole luku")

print("montako lottoriviä haluat arpoa (oletus 1, max 10)?: ")
while luuppimuuttuja:

    try:
        haluttuRivimaaraLukija = input()

        if haluttuRivimaaraLukija == '':
            haluttuRivimaara = 1
        else:
            haluttuRivimaara = int(haluttuRivimaaraLukija)

        if haluttuRivimaara > 0 and haluttuRivimaara < 11:
            luuppimuuttuja = False
        else:
            print("luku ulkona 1-10 arvoväliltä")

    except ValueError:
        print("syötetty arvo ei ole luku")

lottonumerot = []

for kierrokset in range(haluttuRivimaara):
# Arvotaan numerot.
    lottonumerot.append(arpakone.arvo(sekoitukset))

# Printataan arvotut numerot konsoliin.
print()
for element in lottonumerot:
    print ( element )

# Tallennetaan tulokset tiedostoon
tiedosto.tallenna_lottonumerot(lottonumerot)

print("haluatko tulostaa kaikki tallennetut rivit?")
tulostuksenValinta = input("k = kyllä, e = ei : ")
if tulostuksenValinta == 'k':
    print("\n\nkaikki tallennetut arvotut rivit:")
    tiedosto.lue_lottonumerot()
elif tulostuksenValinta == 'e':
    print("kiitos käytöstä. Heippa.")
else: print("ei ymmärrä, heidå")