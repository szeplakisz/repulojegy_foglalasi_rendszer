from rendszer import FoglalasiRendszer

def menu():
    print("\nRepülőjegy Foglalási Rendszer")
    print("1. Jegy foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Járatok listázása")
    print("0. Kilépés")

def main():
    rendszer = FoglalasiRendszer()
    while True:
        menu()
        valaszt = input("Válassz egy műveletet: ")
        if valaszt == "1":
            utas_nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járatszámot: ")
            datum = input("Add meg az utazás dátumát (YYYY-MM-DD): ")
            eredmeny = rendszer.jegy_foglalasa(utas_nev, jaratszam, datum)
            print(eredmeny)
        elif valaszt == "2":
            utas_nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járatszámot: ")
            datum = input("Add meg a foglalás dátumát (YYYY-MM-DD): ")
            eredmeny = rendszer.foglalas_lemondasa(utas_nev, jaratszam, datum)
            print(eredmeny)
        elif valaszt == "3":
            print("\nAktuális foglalások:")
            for f in rendszer.foglalasok_listazasa():
                print(f)
        elif valaszt == "4":
            print("\nElérhető járatok:")
            for j in rendszer.legitarsasag.listaz_jaratok():
                print(j)
        elif valaszt == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás, próbáld újra!")

if __name__ == "__main__":
    main()