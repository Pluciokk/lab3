
n = int(input("Podaj numer podpunktu : "))

if n == 1:
    print("Pkt.1")
    imie = input("Podaj imie : ")
    print(f"Witaj {imie}")

elif n == 2:
    print("Pkt.2")
    wiek = int(input("Podaj wiek : "))
    print(f"Twoj wiek to {wiek}")

elif n == 3:
    print("Pkt.3")
    imie = input("Podaj imie : ")
    nazwisko = input("Podaj nazwisko : ")
    print("Twoje inicjaly to : ",imie[0].upper(),nazwisko[0].upper())

elif n == 4:
    print("Pkt.4")
    lancuch = input("Podaj lancuch znaków : ")
    for i in range(5):
        print(lancuch)

elif n == 5:
    print("Pkt.5")
    lancuch1 = input("Podaj lancuch znaków 1 : ")
    lancuch2 = input("Podaj lancuch znaków 2 : ")
    lancuch3 = lancuch1 + lancuch2
    print(lancuch3)

elif n == 6:
    print("Pkt.6")
    lancuch1 = input("Podaj lancuch znaków 1 : ")
    lancuch2 = input("Podaj lancuch znaków 2 : ")
    print(lancuch1[:len(lancuch1)//2]+lancuch2[len(lancuch2)//2:])
else:
    print("Podano nieprawidłowy podpunkt.")





