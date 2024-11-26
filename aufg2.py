
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

# Aufgabe 3 & 4
vname = ("Nico")
nname =("Kruse")
ausb =("Software Developer")
zitat =("Will somebody get this big walking carpet out of my way?!")

print(f"Hey, my name is {vname} {nname}. \nI just recently started my journey as a {ausb}.\n")
print(f"Here's a quote from one fo my favourite movies. Can you guess which one?\n\"{zitat}\"")

# Aufgabe 5
print("Hallo")
bname =str(input("Bitte geben deinen Namen ein: "))
balter =int(input("Bitte gebe dein Alter ein: "))
bberuf =str(input("Welchen Beruf hast du? "))

print(f"Danke für die Info {bname}.\nDass du im stolzen Alter von {balter} Jahren noch als {bberuf} tätig bist, ist eine tolle Leistung. Respekt!")

# Aufgabe 6
nurzahl =str(input("Bitte gebe eine Ziffernfolge ein: "))
if nurzahl.isdigit():
    print("Danke.")
else:
    print("Bitte gebe nur Ziffern ein, keine Buchstaben und Sonderzeichen.")

# Aufgabe 7
ganzzahl = int(36)
kommazahl = float(172.56)
zeichen = str("buchstaben")
logisch = bool(True)

print(ganzzahl, type(ganzzahl))
print(kommazahl, type(kommazahl))
print(zeichen, type(zeichen))
print(logisch, type(logisch))

# Aufgabe 8
ganzezahl = int(3978)
zahlmitkomma = float(ganzezahl)
zahlalstext = str(ganzezahl)
print(ganzezahl)
print(zahlmitkomma)
print(zahlalstext)

# Aufgabe 9.1/9.2/9.3
while True:
    try:
        zahleing = float(input("Bitte gebe eine Zahl ein, die durch 2 geteilt werden soll: "))
        if zahleing < 0:
            print("Die Zahl darf nicht negativ sein!")
        elif zahleing == 0:
            print("Teilung durch 0 nicht erlaubt!")
        else:
            ergebnis = float(zahleing / 2)
            print(f"{zahleing} geteilt durch 2 ist: {ergebnis}!")
            break
    except ValueError:
        print("Bitte gebe eine gültige Zahl ein.")





