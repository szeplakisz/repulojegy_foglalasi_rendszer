class JegyFoglalas:
    def __init__(self, utas_nev, jarat, datum):
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.datum = datum

    def informacio(self):
        return f"{self.utas_nev} - {self.jarat.jaratszam} ({self.jarat.celallomas}) - {self.datum} - {self.jarat.jegyar} Ft"