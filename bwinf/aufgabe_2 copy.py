#open text
text = open("praeferenzen0.txt", "r")
first_Line = text.readline() #read first line of file
print(first_Line)

first_Line = first_Line.split() #first line is split
anzahl_Personen = int(first_Line[0]) #use index of the first line to define the number of persons as int
anzahl_Termine = int(first_Line[1]) #use index of the first line to define the number of dates as int

x = 0 #define variable, thats being used later on
praeferenz_Summe = [] #create a list with which the sum can be calculated later
for i, zeile in enumerate(text): #every line is being scanned while the text is being enumerated --> is now iterable
    praeferenz_Zeile = [] #make another list to get a 2d array later
    for j in range(anzahl_Termine): #for every person append the just created list with fitting preference, 0, 1 or 2
        praeferenz_Zeile.append([int(zeile.rstrip().split()[x])]) #make the array 3d to get access to all values --> d1 = all values, 2d = one line, 3d = value
        x += 1 #to move forward in the line (index)
    x = 0 #set it back to 0 to begin with a new line
    praeferenz_Summe.append(praeferenz_Zeile) #append the main list with the sublists to get the wanted array
print(praeferenz_Summe)
print("---------------")
text.close()
text = open("praeferenzen4.txt","r")
text.readline()

i = 1
j = 0
k = 0
x = 0
amount = 0
changes = []

 
for k in range(anzahl_Termine):
    for i in range(anzahl_Personen):
        for j in range(anzahl_Termine):
            if praeferenz_Summe[i][x]>praeferenz_Summe[i][j]:
                amount += 1
                break
            else: 
                pass
            
    changes.append(amount)
    x += 1
    amount = 0
print(changes)
if changes != []:
        m = changes[0]
        for n in changes:
            if n <=m:
                m = n  
print(m)
pos_PD = changes.index(m)+1
print("Der beste Tag ist der", pos_PD,". Tag. Es müssen", m, "Änderungen vorgenommen werden.")