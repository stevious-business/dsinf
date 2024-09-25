if __name__ == "__main__":
    gewicht = float(input("Bitte geben Sie Ihr Gewicht in kg an: "))
    hoehe = float(input("Bitte geben Sie Ihre Höhe in m an: "))
    bmi = gewicht/hoehe**2
    wertung_m = wertung_w = "durchschnittlich"
    if bmi <= 19:
        wertung_w = "untergewichtig"
        wertung_m = "untergewichtig"
    elif bmi <= 20:
        wertung_m = "untergewichtig"
    elif bmi >= 25:
        wertung_w = "übergewichtig"
        wertung_m = "übergewichtig"
    elif bmi >= 24:
        wertung_w = "übergewichtig"
    print(f"Ihr BMI beträgt {round(bmi, 2)}.", end=" ")
    print(f"Als Mann sind Sie damit {wertung_m}, als Frau {wertung_w}.")
