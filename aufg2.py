# Aufgabe 1.1
startwert = 10
zwischenwert = startwert + 5
endwert = zwischenwert * 2
print(startwert, zwischenwert,endwert)

# Aufgabe 2.1
Zahleing = int(input("Gebe eine Zahl ein:"))
if Zahleing % 2 == 0:
    print("gerade Zahl")
else:
    print("ungerade Zahl")

# Aufgabe 2.2
Zahleing = int(input("Gebe eine Zahl ein:"))
if Zahleing < 100:
    print("kleiner 100")
elif Zahleing == 100:
    print("genau 100")
else:
    print("groesser 100")

# Aufgabe 2.3
passwort = "1234567" # besser mit Datenbank und/oder Hash natürlich
while True:
    pweingabe = str(input("Gebe das Passwort ein:"))
    if pweingabe != passwort:
        print("Passwort falsch - erneut versuchen!")
    else:
        print("Passwort korrekt!")
        break

# Aufgabe 2.4
Zahleing = int(input("Gebe eine Zahl ein:"))
if 50 < Zahleing < 100:
    print("innerhalb 50 und 100")
else:
    print("ausserhalb 50 bis 100")

# Aufgabe 2.5
freigabe = int(input("Gebe dein Alter ein:"))
if freigabe < 16:
    print("Du bist zu jung für den Führerschein.")
elif 16 == freigabe <= 18:
    print("Du darfst einen Führerschein machen.")
else:
    print("Du darfst Auto fahren.")

# Aufgabe 2.6
def zahlenvergleich():
    zAeingabe = int(input("Gebe die erste Zahl ein:"))
    zBeingabe = int(input("Gebe die zweite Zahl ein:"))
    if zAeingabe == zBeingabe:
        print("Beide Zahlen sind gleich groß.")
    elif zAeingabe > zBeingabe:
        print("Die erste Zahl ist größer als die zweite.")
    else:
        print("Die erste Zahl ist kleiner als die zweite.")
    zABsumme = zAeingabe + zBeingabe
    if zABsumme % 2 == 0:
        print(f"Die Summe aus {zAeingabe} und {zBeingabe} ist gerade.")
    else:
        print(f"Die Summe aus {zAeingabe} und {zBeingabe} ist ungerade.")
zahlenvergleich()

