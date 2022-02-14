#Zeile 0: a[0][0]+a[0][1]a[0][2]
#Zeile 1: a[1][0]+a[1][1]a[1][2]
#Zeile 2: a[2][0]+a[2][1]a[2][2]
#Spalte 0: a[0][0]+a[0][1]a[0][2]
#Spalte 1: a[1][0]+a[1][1]a[1][2]
#Spalte 2: a[2][0]+a[2][1]a[2][2]
#Diagnoale 1: a[0][0]+a[1][1]a[2][2]
#Diagnoale 2: a[2][0]+a[1][1]a[0][2]


a = [[5, 10, 3],[4, 6, 8],[9, 2, 7]]
#a=[[5,10,3],[4,6,8],[9,2,8]]
#a=[[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]

sum = 0
rSum=[]
cSum=[]
d1Sum = 0
d2Sum = 0

x = 0
y = len(a[0])-1
zeilen = len(a)
spalten = len(a[0])


def zeilenSumme(sum):
    for i in range(zeilen):
        for j in range(spalten):
            sum += a[i][j]
        rSum.append(sum)
        sum = 0
    print(rSum)

def spaltenSumme(sum):
    for i in range(spalten):
        for j in range(zeilen):
            sum += a[j][i]
        cSum.append(sum)
        sum = 0
    print(cSum)
    

def diagnoal1(d1Sum, x):
    for i in range(zeilen):
        d1Sum += a[i][x]
        x += 1
    print(d1Sum)
    return d1Sum

def diganoal2(d2Sum, y):
    for i in range(zeilen):
        d2Sum += a[i][y]
        y -= 1
    print(d2Sum)
    return d2Sum

def magischeZahlBerechnen(rSum, cSum, d1Sum, d2Sum):
    magicNumber = []
    result = False
    if len(rSum)>0:
        result = all(elem == rSum[0] for elem in rSum)
    if result:
        magicNumber.append(rSum[0])
    result = False
    if len(cSum)>0:
        result = all(elem == cSum[0] for elem in cSum)
    if result:
        magicNumber.append(cSum[0])
    
    magicNumber.append(d1Sum)
    magicNumber.append(d2Sum)

    result = False
    if len(magicNumber)>0:
        result = all(elem == magicNumber[0] for elem in magicNumber)
    if result:
        print('The magic number is:', magicNumber[0])

zeilenSumme(sum)
spaltenSumme(sum)
d1Sum = diagnoal1(d1Sum, x)
d2Sum = diganoal2(d2Sum, y)
magischeZahlBerechnen(rSum, cSum, d1Sum, d2Sum)