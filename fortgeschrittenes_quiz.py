FRAGE = "Computersprachen können interpretiert oder kompiliert sein. Wahr oder Falsch: Python ist eine interpretierte Sprache."
ANTWORT = "wahr"

spieler_name = input("Wie heißt du? ")
print("Willkommen zum Quiz-Spiel,", spieler_name + "!")

while True:
    print(FRAGE)
    spieler_punkte = 0
    versuch_anzahl = 0
    while versuch_anzahl < 3:
        antwort = input("Antwort: ").lower()
        if antwort == ANTWORT:
            spieler_punkte += 1
            print("Richtig!!!")
        else:
            print("Leider Falsch! Versuche es nochmal.")
        versuch_anzahl += 1
    print("Glückwunsch,", spieler_name + "! Du hast", spieler_punkte, "Punkte erzielt.")
    print("Schreibe 'nochmal', um nochmal zu spielen, oder drücke ENTER, um das Spiel zu beenden:")
    if not input():
        break
