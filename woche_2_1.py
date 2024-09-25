if __name__ == "__main__":
    hoehe, breite, tiefe = float(input("Höhe: ")), float(input("Breite: ")), float(input("Tiefe: "))
    a = abs(hoehe)
    b = abs(breite)
    c = abs(tiefe)
    Ao = 2*a*b+2*b*c+2*a*c
    V = a*b*c
    print(f"Volumen: {V} und Oberflächeninhalt: {Ao}")
