import datetime

teilnehmer = 1
alter = int() # das Alter
groesse = float() # Koerpergroesse in meter
nachname = str() # der Nachname
hobby = str() # Hobbies
langhobb = int() # Anzahl der eingegebenen Hobbies
vstatus = bool() # Status verheiratet oder nicht
hobbies = list() # Taetigkeiten


def eingabe():
    global teilnehmer, nachname, alter, groesse, vstatus, hobbies, langhobb
    print(f"Teilnehmer:{teilnehmer}")
    nachname = input("Nachname eingeben: ")
    geburt = int(input("Geburtsjahr eingeben: "))
    heute = datetime.datetime.now()
    alter = heute.year - geburt
    groesse = input("Koerpergroesse in Meter: ")
    married = input("verheiratet (j/n): ")
    if married == "j":
        vstatus = True
    hobby = input("Nenne Hobbies mit Komma getrennt: ")
    hobbies = hobby.split(",")
    langhobb = len(hobbies)

    '''def listeschreiben():
        daten = [nachname, alter, groesse, married]
    listeschreiben()'''

def zeigetabelle():
    if vstatus == True:
        verheir = "verheiratet"
    else:
        verheir = "ledig"
    print("Tab:\tNachname\tAlter\tGröße\tStatus")
    print(f"TN {teilnehmer}:\t {nachname} \t {alter} Jahre\t {groesse} Meter\t {verheir}")
    print(f"Insgesamt {langhobb} Hobbies: {hobbies}")


eingabe()

zeigetabelle()