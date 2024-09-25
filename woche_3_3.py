if __name__ == "__main__":
    kreditbetrag = float(input("Kreditbetrag in EUR: "))
    zinssatz = float(input("Zinslsatz in Prozent: "))/100
    rueckzahlung = float(input("Rückzahlungsbetrag in EUR: "))
    year = 0
    while kreditbetrag > 0:
        zinsen = zinssatz*kreditbetrag
        tilgung = rueckzahlung - zinsen
        print(f"\nZustand am Anfang von Jahr {year}:")
        print("Restschulden:", kreditbetrag)
        print("Zinsen:", zinsen)
        print("Tilgung:", tilgung)
        kreditbetrag -= tilgung
        year += 1
    print(f"Nach {year} Jahren sind alle Schulden abbezahlt")
