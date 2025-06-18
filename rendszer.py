from legitarsasag import LegiTarsasag
from jarat import BelfoldiJarat, NemzetkoziJarat
from jegyfoglalas import JegyFoglalas
from datetime import datetime

class FoglalasiRendszer:
    def __init__(self):
        self.legitarsasag = LegiTarsasag("DemoAir")
        self.foglalasok = []
        self._elore_betoltott_adatok()

    def _elore_betoltott_adatok(self):
        j1 = BelfoldiJarat("B101", "Budapest", 15000)
        j2 = NemzetkoziJarat("N201", "London", 50000)
        j3 = NemzetkoziJarat("N202", "Berlin", 60000)
        self.legitarsasag.jarat_hozzaad(j1)
        self.legitarsasag.jarat_hozzaad(j2)
        self.legitarsasag.jarat_hozzaad(j3)

        self.foglalasok.append(JegyFoglalas("Kiss Ádám", j1, "2025-07-20"))
        self.foglalasok.append(JegyFoglalas("Nagy Zsolt", j2, "2025-08-22"))
        self.foglalasok.append(JegyFoglalas("Tóth Zsombor", j3, "2025-07-01"))
        self.foglalasok.append(JegyFoglalas("Varga Dóra", j1, "2025-07-25"))
        self.foglalasok.append(JegyFoglalas("Szabó Magdolna", j2, "2025-08-28"))
        self.foglalasok.append(JegyFoglalas("Takács Imre", j3, "2025-07-05"))

    def jegy_foglalasa(self, utas_nev, jaratszam, datum):
        jarat = self.legitarsasag.jarat_keres(jaratszam)
        if jarat is None:
            return "Nincs ilyen járat."
        if not self._ervenyes_datum(datum):
            return "Érvénytelen dátum."
        foglalas = JegyFoglalas(utas_nev, jarat, datum)
        self.foglalasok.append(foglalas)
        return f"Sikeres foglalás! Ár: {jarat.jegyar} Ft"

    def foglalas_lemondasa(self, utas_nev, jaratszam, datum):
        for f in self.foglalasok:
            if f.utas_nev == utas_nev and f.jarat.jaratszam == jaratszam and f.datum == datum:
                self.foglalasok.remove(f)
                return "Foglalás sikeresen lemondva."
        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):
        return [f.informacio() for f in self.foglalasok]

    def _ervenyes_datum(self, datum):
        try:
            datum_obj = datetime.strptime(datum, "%Y-%m-%d")
            return datum_obj > datetime.now()
        except ValueError:
            return False