if __name__ == "__main__":
    umsatz = 24_676
    if umsatz > 30_000:
        print(f"Sie erhalten eine Prämie im Wert von {umsatz*0.01}€")
    else:
        print("Sie erhalten leider keine Prämie")
