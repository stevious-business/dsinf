if __name__ == "__main__":
    if True:
        for i in range(11):
            zahl = 10 - i
            print(zahl)
    else:
        # alternative via while:
        i = 10
        while i >= 0: # verhalten bei 0 ist nicht definiert
            i -= 1
            print(i)
