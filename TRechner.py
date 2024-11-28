
rhistory = []

# Rechenoperationen
def rechnen(zahl1, zahl2, ops):
  if ops == "+":
    return zahl1 + zahl2
  elif ops == "-":
    return zahl1 - zahl2
  elif ops == "x":
    return zahl1 * zahl2
  elif ops == "/":
    if zahl2 == 0:
      return "Man kann nicht durch Null teilen!"
    else:
      return zahl1 / zahl2
  elif ops == "^":
    return zahl1 ** zahl2
  elif ops == "Pw":
    return (zahl1 * zahl2) / 100
  elif ops == "%":
    return (zahl2 / zahl1) * 100
  elif ops == "Gw":
    return zahl1 / (zahl2 / 100)



# Bei Eingabe Komma in Punkt umwandeln, Ziffern prüfen, dann in float umwandeln
def eingabe1():
  print(f"Du willst {opname}!")
  while True:
      zahl1str = input(f"Gib {ztxt1} ein: ").replace(",", ".")
      if zahl1str.replace(".", "").replace("-", "").isdigit():
        try:
          int(zahl1str)
          return int(zahl1str) # Ausgabe ohne Kommastellen wenn nicht vorhanden
        except ValueError:
          return float(zahl1str)
      else:
        print("Gültige Zahl eingeben")

def eingabe2():
  while True:
      zahl2str = input(f"Gib {ztxt2} ein: ").replace(",", ".")
      if zahl2str.replace(".", "").replace("-", "").isdigit():
        try:
          int(zahl2str)
          return int(zahl2str)
        except ValueError:
          return float(zahl2str)
      else:
        print("Gültige Zahl eingeben")

# Auswahl der Rechenoperation
while True:
  try:
    print("-" * 60)
    print("1.PLUS \\", "2.MINUS \\", "3.MAL \\", "4.GETEILT \\", "5.POTENZ \\", "6.WURZEL")
    print("7.PROZENTWERT \\", "8.PROZENTSATZ \\", "9.GRUNDWERT \\", "0 zum Beenden")
    print("-" * 60)
    auswahl = int(input("Was willst du rechnen? "))
    if auswahl == 0:
      print("Rechner beendet")
      break
  except ValueError:
      print("Bitte gueltige Zahl eingeben!")
      continue

  def showhistory():
    showhist = " | ".join(reversed(rhistory))
    print("letzte Berechnungen:", showhist)

# Operationen zuweisen, an Funktionen übergegen und Ergebnis erhalten
  if auswahl == 1:
    opname = "addieren"
    ops = "+"
    ztxt1 = "die erste Zahl"
    ztxt2 = "die zweite Zahl"
    zahl1 = eingabe1()
    zahl2 = eingabe2()
    ergebnis = rechnen(zahl1, zahl2, "+")
  elif auswahl == 2:
    opname = "subtrahieren"
    ops = "-"
    ztxt1 = "die erste Zahl"
    ztxt2 = "den Subtrahenden"
    zahl1 = eingabe1()
    zahl2 = eingabe2()
    ergebnis = rechnen(zahl1, zahl2, "-")
  elif auswahl == 3:
    opname = "multiplizieren"
    ops = "x"
    ztxt1 = "die erste Zahl"
    ztxt2 = "den Multiplikator"
    zahl1 = eingabe1()
    zahl2 = eingabe2()
    ergebnis = rechnen(zahl1, zahl2, "x")
  elif auswahl == 4:
    opname ="dividieren"
    ops = "/"
    ztxt1 = "die erste Zahl"
    ztxt2 = "den Teiler"
    zahl1 = eingabe1()
    zahl2 = eingabe2()
    ergebnis = rechnen(zahl1, zahl2, "/")
  elif auswahl == 5:
    opname = "hochrechnen"
    ops = "^"
    ztxt1 = "die erste Zahl"
    ztxt2 = "die Potenz"
    zahl1 = eingabe1()
    zahl2 = eingabe2()
    ergebnis = rechnen(zahl1, zahl2, "^")
  elif auswahl == 6:
    opname = "die Quadratwurzel ziehen"
    ztxt1 = "die Zahl"
    zahl1 = eingabe1()
    ergebnis = zahl1 ** 0.5 #nur Quadratwurzel
    print(f" √{zahl1} = {ergebnis:.2f}")
    rhistory.append(f" √{zahl1} = {ergebnis:.2f}")
    showhistory()
    continue
  elif auswahl == 7:
    opname = "den Prozentwert ermitteln"
    ops = "Pw"
    ztxt1 = "den Grundwert"
    ztxt2 = "die Prozentzahl"
    zahl1 = eingabe1()
    zahl2 = eingabe2()
    ergebnis = rechnen(zahl1, zahl2, "Pw")
    print(f"{zahl2}% von {zahl1} = {ergebnis:.2f}")
    rhistory.append(f"{zahl2}% von {zahl1} = {ergebnis:.2f}")
    showhistory()
    continue
  elif auswahl == 8:
    opname = "den Prozentsatz ermitteln"
    ops = "%"
    ztxt1 = "den Gesamtwert"
    ztxt2 = "den Teilwert"
    zahl1 = eingabe1()
    zahl2 = eingabe2()
    ergebnis = rechnen(zahl1, zahl2, "%")
    print(f"{zahl2} von {zahl1} = {ergebnis:.2f}%")
    rhistory.append(f"{zahl2} von {zahl1} = {ergebnis:.2f}%")
    showhistory()
    continue
  elif auswahl == 9:
    opname = "den Grundwert ermitteln"
    ops = "Gw"
    ztxt1 = "den Teilwert"
    ztxt2 = "den Prozentsatz"
    zahl1 = eingabe1()
    zahl2 = eingabe2()
    ergebnis = rechnen(zahl1, zahl2, "Gw")
    print(f"{zahl1} = {zahl2}% von {ergebnis:.2f}")
    rhistory.append(f"{zahl1} = {zahl2}% von {ergebnis:.2f}")
    showhistory()
    continue
  else:
    print("Waehle von 1 bis 9! (oder 0 zum Beenden)")
    continue

# Ergebnis & Historie anzeigen
  print("_" * 30)
  if isinstance(ergebnis, float):
    print(f"{zahl1} {ops} {zahl2} = {ergebnis:.2f}")
    rhistory.append(f"{zahl1} {ops} {zahl2} = {ergebnis:.2f}")
  else:
    print(f"{zahl1} {ops} {zahl2} = {ergebnis:.0f}")
    rhistory.append(f"{zahl1} {ops} {zahl2} = {ergebnis:.0f}")
  print("_" * 30)
  showhistory()

