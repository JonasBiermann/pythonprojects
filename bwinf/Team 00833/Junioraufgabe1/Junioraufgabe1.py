import math as m # für Wurzel

eingabe = input("Textdatei mit .txt eingeben: ")
eingabe = open(eingabe, "r") # Datei im Read-Modus öffnen

anzahl = eingabe.readline() # erste Zeile einlesen
anzahl = anzahl.split(" ") # einlne Zahlen zur Liste

anzahlH = int(anzahl[0]) # Anzahl der Häuser = erster str aus Liste und wird in int umgewandelt 
anzahlW = int(anzahl[1]) # gleiches für Anzahl Windräder


posGesamt = [] # neue Liste = posGesamt
for zeile in eingabe: # zeilen der Datei einlesen
    posGesamt += zeile.rstrip().split() # eine Zeile wird an Leerzeichen getrennt und zur Liste hinzugefügt

posH = posGesamt[:] # [:] damit posGesamt nicht beeinflusst wird
del posH[anzahlH*2:(anzahlW*2 + anzahlH*2)] # Positionen Windräder werden gelöscht, damit nur Positionen Häuser

posW = posGesamt[:] # gleiches für Positionen von Windrädern
del posW[0:anzahlH*2]


def hoehe(anzahlH, posH, posW, nummerW): # neue Funktion
    nummerH = 0 # Position des ersten Hauses
    while nummerH < anzahlH*2: # solange nicht alle Häuser getestet
        dis = m.sqrt((int(posW[nummerW])-int(posH[nummerH]))**2+(int(posW[nummerW+1])-int(posH[nummerH+1]))**2)
        # Distanz mit Positionen berechnen
        if nummerH == 0:
            dismin = dis # erste Distanz als kleinste Distanz
        if dis < dismin:
            dismin = dis # kleinste Distanz gespeichert
        nummerH += 2 # nächstes Haus
    h = dismin / 10 # Höhe berechnen
    return h # Höhe ausgeben

nummerW = 0 # erstes Windrad
listeH = "" # "normale" Liste für Höhen
for nummerW in range(anzahlW): # alle Windräder testen
    h = hoehe(anzahlH, posH, posW, nummerW*2) # Funktion wird genutzt um Höhe zu berechnen
    if h <= 0:
          listeH += ("Windrad " + str(nummerW+1) + " kann nicht gebaut werden, ")
          # nicht baubares Windrad wird zur "normalen" Liste hinzugefügt
    else:
        listeH += ("Windrad " + str(nummerW+1) + " = " + str(h) + " m, ")
        # Höhe wird zur "normalen" Liste hinzugefügt
listeH = listeH[:(len(listeH)-2)] # letztes Komma wird gelöscht
print("Maximale Höhen:\n", listeH)