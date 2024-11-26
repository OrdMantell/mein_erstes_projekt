
# Aufgabe 1
xy = 1
while True:
    print(xy)
    xy += 1
    if xy > 10:
        break


# Aufgabe 2
zaehler = 1
addierer = int()
print("Gebe Zahlen zum addieren ein. Gib 0 ein um zu abzuschliessen.")
while True:
    yz = int(input(f"Gebe die {zaehler}. Zahl ein: "))
    if yz == 0:
        print(f"Die Summe ist: {addierer}.")
        break
    zaehler += 1
    addierer = addierer + yz


# Aufgabe 3
PASSWORT = str("knucklehead74")
while True:
    passwort = input("Bitte gebe das Passwort ein: ")
    if passwort == PASSWORT:
        print("Richtig, danke!")
        break
    else:
        print("Falsches Passwort! Versuche es erneut!")

# Aufgabe 4