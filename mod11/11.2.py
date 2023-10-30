class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kulje(self, aika):
        self.matka = self.matka + (aika * self.nopeus)
        return


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka, akku_kw,):
        self.akku_kw = akku_kw
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)

        def kulje(self, aika):
            super().kulje(aika)


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka, bensa_ltr):
        self.bensa_ltr = bensa_ltr
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)
    def kulje(self,aika):
        super().kulje(aika)

shk = Sähköauto("ABC-15", 180, 85, 0, 52.5)
plt = Polttomoottoriauto("ACD-123", 165, 63, 0, 32.3)
