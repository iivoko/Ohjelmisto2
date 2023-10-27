class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeus):
        self.tämänhetkinen_nopeus = self.tämänhetkinen_nopeus + nopeus

        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
        return


auto = Auto("ABC-123", "142 km/h", 0, 0)


auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print(f"auton nopeus on {auto.tämänhetkinen_nopeus}km/h")

auto.kiihdytä(-200)

print(f"auton nopeus on {auto.tämänhetkinen_nopeus}km/h")
