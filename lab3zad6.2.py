loop = True
while loop:
    dana = int(input("Podaj liczbe calkowita : "))
    if dana >= 0:
        print(dana ** 2)
    else:
        loop = False
        print("Dziekujemy za skorzystanie z naszej aplikacji.")
        continue
