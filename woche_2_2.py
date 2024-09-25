if __name__ == "__main__":
    alter = int(input("Geben Sie Ihr Alter an: "))
    if alter < 18:
        print("Der Preis für Personen unter 18 beträgt 2,50€")
    else:
        print("Der Preis für Erwachsene beträgt 4,00€")
