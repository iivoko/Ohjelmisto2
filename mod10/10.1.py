class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = alin

    def kerros_ylös(self):
        self.sijainti = self.sijainti + 1
        if self.sijainti > self.ylin:
            self.sijainti = self.ylin
        print(self.sijainti)
        return

    def kerros_alas(self):
        self.sijainti = self.sijainti - 1
        if self.sijainti < self.alin:
            self.sijainti = self.alin
        print(self.sijainti)
        return

    def siirry_kerrokseen(self, kohde):
        while self.sijainti < kohde:
            self.kerros_ylös()
        while self.sijainti > kohde:
            self.kerros_alas()
        print("hissi on nyt kohteessa")
        return

hissi = Hissi(1, 6)

hissi.siirry_kerrokseen(6)