
# Aufgabe 1 mit while zählen
xy = 1
while True:
    print(xy)
    xy += 1
    if xy > 10:
        break


# Aufgabe 2 Eingabe addieren
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


# Aufgabe 3 Passwortabfrage
PASSWORT = str("knucklehead74")
while True:
    passwort = input("Bitte gebe das Passwort ein: ")
    if passwort == PASSWORT:
        print("Richtig, danke!")
        break
    else:
        print("Falsches Passwort! Versuche es erneut!")


# Aufgabe 4 mit for zählen
for i in range(1, 11):
    print(i)


# Aufgabe 5a gerade Zahle ausgeben
for gerade in range(1, 21):
    if gerade % 2 == 0:
        print(gerade)


# Aufgabe 5b jeden 5ten Index ausgeben
zliste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
for f in range(4, len(zliste), 5):
    print(zliste[f])


# Aufgabe 6 Rechteck aus Sternen
vertik = 5
horiz = 5
for r in range(horiz):
    print("*" * vertik)

# Alternativ 6 mit Verschachtelung
for ho in range(horiz):
    for ve in range(vertik):
        print("*", end="")
    print()

# Überlegung zu 6: Rechteck Umrandung
vertik = 7
horiz = 6
for r in range(horiz):
    if r == 0 or r == horiz - 1: # erste/letzte Reihe alles Sterne
        print("* " * vertik)
    else:
        print("* " + "  " * (vertik - 2) + "* ") # nur erste/letze Spalte Sterne


# Aufgabe 7 rückwärts iteration
for backw in range(10, 0, -1): #dritte Stelle für Schritte
    print(backw)


# Aufgabe 8 Listen erstellen und manipulieren
lnamen = ["Anna", "Max", "Tom", "Lisa"]
print("Es sind", len(lnamen), "Namen in der Liste:", (lnamen))
lnamen.append("Marie")
print("Es sind", len(lnamen), "Namen in der Liste:", (lnamen))
lnamen.remove("Tom")
print("Es sind", len(lnamen), "Namen in der Liste:", (lnamen))


# Aufgabe 9 Listen sortieren und umkehren
lnummern = [5, 3, 8, 1, 2]
lnummern.reverse()
print("rückwärts:", lnummern) # muss VOR sort passieren
lnummern.sort()
print("aufsteigend:", lnummern)
lnummern.sort(reverse=True)
print("absteigend:", lnummern)

# Überlegung zu 9 Liste lokal um .sort zu umgehen
def aufst(lnummern):
    bnummern = lnummern.copy()
    bnummern.sort()
    print("aufsteigend:", bnummern)
def abst(lnummern):
    bnummern = lnummern.copy()
    bnummern.sort(reverse=True)
    print("absteigend:", bnummern)
def backw(lnummern):
    bnummern = lnummern.copy()
    bnummern.reverse()
    print("rückwärts:", bnummern)
aufst(lnummern)
abst(lnummern)
backw(lnummern)


# Aufgabe 10 Listen Methoden
lzahlen = [1, 2, 3, 4, 5]
lzahlen.append(6)
lzahlen.insert(0, 0)
tres = lzahlen.count(3)
print("Die Liste:", lzahlen, "enthält", len(lzahlen), "Einträge.")
print("Die Zahl drei kommt", tres, "mal vor.")


# Aufgabe 11 & 12 Listen Iteration und Summe
lzehner = [10, 20, 30, 40, 50]
esumme = 0
for eintrag in lzehner:
    print(eintrag)
for eintrag in lzehner:
    esumme += eintrag
print("Summe der Liste=", esumme)


# Aufgabe 13 Iteration String
wort = str(input("Wort eingeben:"))
for buchst in wort:
    print(buchst)
print(" - ".join(wort)) # in einer Zeile mit - dazwischen


# Aufgabe 14 & 15 & 16 Liste filtern, Indizes, enumerate
lzahlen = [3, 45, 23, 7, 36, 2]
for mehralszehn in lzahlen:
    if mehralszehn > 10:
        print(mehralszehn)
print("for-if:")
for idx in range(len(lzahlen)): #für jeden index ausgeben
    print(f"Index: {idx} hat den Wert {lzahlen[idx]}") #wert des entspr. index
print("for-enumerate:")
for idx, wert in enumerate(lzahlen): #verbindet index mit wert in liste
    print(f"Index: {idx} hat den Wert {wert}") #index und wert als touple

