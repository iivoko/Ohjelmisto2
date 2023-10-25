class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

auto = Auto("ABC-123", "142 km/h", 0, 0)

print(f"auton rekisteritunnus on {auto.rekisteritunnus},huippunopeus {auto.huippunopeus}, tämänhetkinen nopeus {auto.tämänhetkinen_nopeus}, kuljettu matka {auto.kuljettu_matka} ")