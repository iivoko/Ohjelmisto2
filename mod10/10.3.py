class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = alin

    def kerros_ylös(self):
        self.sijainti = self.sijainti + 1
        print(self.sijainti)
        return

    def kerros_alas(self):
        self.sijainti = self.sijainti - 1
        print(self.sijainti)
        return

    def siirry_kerrokseen(self, kohde):
        while self.sijainti < kohde:
            self.kerros_ylös()
        while self.sijainti > kohde:
            self.kerros_alas()
        if self.sijainti > self.ylin:
            self.sijainti = self.ylin
        elif self.sijainti < self.alin:
            self.sijainti = self.alin
        return


class Talo:
    def __init__(self, alin, ylin, hissit):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissit):
            hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissinro, kohde):
        hissi = self.hissit[hissinro - 1]
        hissi.siirry_kerrokseen(kohde)
        print(f"Hissi {hissinro} on nyt siirtynyt kerrokseen {kohde}")
        return

    def palohälytys(self):
        print("Palohälytys soi. Siirretään hissit alas")
        for i, hissi in enumerate(self.hissit):
            self.aja_hissia(i + 1, self.alin)
        print("Kaikki hissit on nyt siirretty alas")
        return

talo = Talo(1, 10, 5)
talo.aja_hissia(1,3)
talo.aja_hissia(2,4)
talo.aja_hissia(3,2)
talo.aja_hissia(4,9)
talo.aja_hissia(5,7)
talo.palohälytys()