parkplatz = open('parkplatz0.txt', "r").readlines()

erstes_auto = parkplatz[0][0]
letztes_auto = parkplatz[0][2]
anzahl_autos_normal = ord(letztes_auto) - ord(erstes_auto) + 1
anzahl_quer = int(parkplatz[1])


Quer = []
for i in range(anzahl_quer):
    auto = parkplatz[2+i][0]
    position = int(parkplatz[2+i][2:len(parkplatz[2+i])-1])
    Quer += [[chr(i+anzahl_autos_normal+65)]+[position]+[position+1]]



blockierte_Autos = []
Blockierungen = []

for i in range(anzahl_autos_normal):
    for k in Quer:
        for j in k:
            if j == i:
                blockierte_Autos += [chr(i+65)]
                Blockierungen += [[chr(i+65), "wird blockiert durch", k[0]]]
            else:
                pass




Spielraum = []

for i in range(anzahl_quer):
    if i < len(Quer) - 1:
        rechts = abs(Quer[i][2] - Quer[i+1][1]) - 1
    else:
        rechts = anzahl_autos_normal - 1 - Quer[i][2]
    if i > 0:
        links = Quer[i][1] - Quer[i-1][2] - 1
    else:
        links = Quer[i][1]
    Spielraum += [[Quer[i][0], links, rechts]]




index = -1
for i in range(anzahl_autos_normal):
    if chr(i+65) in blockierte_Autos:
        index += 1
        blockiert = Blockierungen[index][0]
        position = ord(blockiert) - 65

        blockierend = Blockierungen[index][2]

        for k in Quer:
            if blockierend in k:
                if k[1] == position:
                    links = 2
                    rechts = 1
                else:
                    links = 1
                    rechts = 2
                blockierend = [blockierend, links, rechts]

        for k in Spielraum:
            if blockierend[0] in k:
                if blockierend[1] < blockierend[2]:
                    if k[1] >= blockierend[1]:
                        print(chr(i+65) + ": " + blockierend[0] + " " + str(blockierend[1]) + " links")
                    elif k[2] >= blockierend[2]:
                        print(chr(i+65) + ": " + blockierend[0] + " " + str(blockierend[2]) + " rechts")

                elif blockierend[1] > blockierend[2]:
                    if k[2] >= blockierend[2]:
                        print(chr(i+65) + ": " + blockierend[0] + " " + str(blockierend[2]) + " rechts")
                    elif k[1] >= blockierend[1]:
                        print(chr(i+65) + ": " + blockierend[0] + " " + str(blockierend[1]) + " links")

                if blockierend[1] > k[1] and blockierend[2] > k[2]:
                    nummer_quer = ord(blockierend[0])-65-anzahl_autos_normal
                    links = [0, ""]
                    rechts = [0, ""]
                    beste_lösung = ""

                    zu_bewegen = 0
                    for j in range(nummer_quer+1):
                        if links[0] < blockierend[1]:
                            if nummer_quer-j < 0:
                                pass
                            else:
                                zu_bewegen += 1
                                string_links = chr(ord(blockierend[0])-j) + " " + str(blockierend[1]-links[0]) + " links, " + links[1]
                                links_neu = int(links[0] + Spielraum[nummer_quer-j][1])
                                links = [links_neu, string_links, zu_bewegen]

                    zu_bewegen = 0
                    for j in range(nummer_quer, anzahl_quer):
                        if rechts[0] < blockierend[2]:
                            if nummer_quer+j > anzahl_quer-1:
                                pass
                            else:
                                zu_bewegen += 1
                                string_rechts = chr(ord(blockierend[0])+j) + " " + str(blockierend[2]-rechts[0]) + " rechts, " + rechts[1]
                                rechts_neu = rechts[0] + Spielraum[nummer_quer+j][2]
                                rechts = [rechts_neu, string_rechts, zu_bewegen]

                    if links[0] >= blockierend[1] and rechts[0] >= blockierend[2]:
                        if links[2] <= rechts[2]:
                            beste_lösung = links[1][0:len(links[1])-2]
                        elif links[2] > rechts[2]:
                            beste_lösung = rechts[1][0:len(rechts[1])-2]

                    elif links[0] >= blockierend[1]:
                            beste_lösung = links[1][0:len(links[1])-2]

                    elif rechts[0] >= blockierend[2]:
                            beste_lösung = rechts[1][0:len(rechts[1])-2]

                    elif links[0] < blockierend[1] and rechts[0] < blockierend[2]:
                        beste_lösung = "Kann nicht ausgeparkt werden"

                    print(chr(i+65) + ": " + beste_lösung)

            else:
                pass

    else:
        print(chr(i+65) + ":")
