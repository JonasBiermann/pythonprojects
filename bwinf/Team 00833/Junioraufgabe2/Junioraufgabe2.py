eingabe = open('praeferenzen0.txt', 'r')
zeile_1 = eingabe.readline()
zeile_1 = zeile_1.split()

personen_Anzahl = int(zeile_1[0])
termin_Anzahl = int(zeile_1[1])

x = 0
ges_Status = []

for i, zeile in enumerate(eingabe):
    zeilen_Status = []
    for j in range(termin_Anzahl):
        zeilen_Status.append([int(zeile.rstrip().split()[x])])
        x += 1
    x = 0
    ges_Status.append(zeilen_Status)

anzahl_aenderungen = 0
aenderungen_liste = []

for k in range(termin_Anzahl):
    for l in range(personen_Anzahl):
        for m in range(termin_Anzahl):
            if ges_Status[l][x]>ges_Status[l][m]:
                anzahl_aenderungen += 1
                break
            else: pass
    aenderungen_liste.append(anzahl_aenderungen)
    x += 1
    anzahl_aenderungen = 0

min_aenderungen = min(aenderungen_liste)
pos_termin = aenderungen_liste.index(min_aenderungen)+1
print('Der beste Termin ist der', pos_termin, '. Tag, es müssen', min_aenderungen, 'vorgenommen werden.')