# lottoarpoja sisältää arpakone-luokan. Arpakone-olio arpoo __valitaan muuttujan
# mukaisen määrän numeroita __palloja muuttujan määrästä numeroita.
# Numerointi alkaa 1:stä.

import random

class arpakone:

    def __init__(self):

        self.__palloja = 40
        self.__valitaan = (7, 1)


    # arvo metodille voi antaa yhden parametrin sisään. Oletusarvo 4.
    # Sekoitusmäärä on pallojen sekoitusten määrä ennen kuin pallo valitaan.
    def arvo(self, sekoitusmaara=4):
        
        # Rivi listaan otetaan arvotut numerot talteen, lisanro muuttujaan lisänumerot.
        rivi = []
        lisanro = []

        # Luodaan muuttuja numerot, johon luodaan pelipallojen numerot
        numerot = []

        # Pistetään sopiva määrä palloja koneeseen.
        for i in range (self.__palloja):
            numerot.append(i + 1)

        # Valitaan pelityypin mukainen määrä numeroita.
        for i in range (self.__valitaan[0]):

            # Sekoitetaan pallot joka valinnan aluksi sekoitusmaara -muuttujan
            # tarjoaman määrän verran.
            for y in range(sekoitusmaara):
                random.shuffle(numerot)

            # Valitaan satunnaisesta indexistä numero pop-metodilla rivi-listalle.
            # Satunnaisen indexin yläpään rajana pallojen määrä miinus for-loopin
            # kierrosnumero.
            rivi.append(numerot.pop(random.randrange(0, self.__palloja-i)))

        # Valitaan pelityypin mukainen määrä lisänumeroita.
        for i in range (self.__valitaan[1]):

            # Sekoitetaan pallot joka valinnan aluksi sekoitusmaara -muuttujan
            # tarjoaman määrän verran

            for y in range(sekoitusmaara):
                random.shuffle(numerot)

            # Valitaan satunnaisesta indexistä numero pop-metodilla rivi-listalle.
            # Satunnaisen indexin yläpään rajana pallojen määrä miinus for-loopin
            # kierrosnumero. Lisäksi vähennetään jo varsinaiset valittujen pallojen määrä.

            lisanro.append(numerot.pop(random.randrange(0, self.__palloja - self.__valitaan[0]-i)))
        
        # Heivataan käyttämättömät numerot
        del numerot

        # Järjestetään rivi ja lisänumerot nousevaan järjestykseen.
        rivi.sort()
        lisanro.sort()

        return rivi, lisanro
        