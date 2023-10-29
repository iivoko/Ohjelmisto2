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
        print("hissi on nyt kohteessa")
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
        for hissi in self.hissit:
            talo.aja_hissia(hissi, self.alin)
        return


talo = Talo(1, 10, 5)
