'''
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
for i in range(1, 11):
    print(i)

# Aufgabe 5a
for gerade in range(1, 21):
    if gerade % 2 == 0:
        print(gerade)

# Aufgabe 5b
zliste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
for f in range(4, len(zliste), 5):
    print(zliste[f])
'''
# Aufgabe 6
vertik = 5
horiz = 5
for r in range(vertik):
    print("*" * horiz)

# Überlegung zu 6: Rechteck Umrandung
vertik = 7
horiz = 6
for r in range(horiz):
    if r == 0 or r == horiz - 1: # erste/letzte Reihe alles Sterne
        print("* " * vertik)
    else:
        print("* " + "  " * (vertik - 2) + "* ") # nur erste/letze Spalte Sterne

# Aufgabe 7
for backw in range(10, 0, -1):
    print(backw)

# Aufgabe 8
lnamen = ["Anna", "Max", "Tom", "Lisa"]
print("Es sind", len(lnamen), "Namen in der Liste:", (lnamen))
lnamen.append("Marie")
print("Es sind", len(lnamen), "Namen in der Liste:", (lnamen))
lnamen.remove("Tom")
print("Es sind", len(lnamen), "Namen in der Liste:", (lnamen))

# Aufgabe 9
lnummern = [5, 3, 8, 1, 2]
lnummern.reverse()
print("rückwärts:", lnummern) # muss VOR sort passieren
lnummern.sort()
print("aufsteigend:", lnummern)
lnummern.sort(reverse=True)
print("absteigend:", lnummern)

# Aufgabe 10
lzahlen = [1, 2, 3, 4, 5]
lzahlen.append(6)
lzahlen.insert(0, 0)
tres = lzahlen.count(3)
print("Die Liste:", lzahlen, "enthält", len(lzahlen), "Einträge.")
print("Die Zahl drei kommt", tres, "mal vor.")