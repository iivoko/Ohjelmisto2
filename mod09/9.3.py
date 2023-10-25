class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeus):
        self.tämänhetkinen_nopeus = self.tämänhetkinen_nopeus + nopeus
        return

    def kulje(self, aika):
        self.kuljettu_matka = aika * self.tämänhetkinen_nopeus
        return

auto = Auto("ABC-123", "142 km/h", 0, 0)


auto.kiihdytä(80)
auto.kulje(3)

print(f"auto on kulkenut {auto.kuljettu_matka}km")
