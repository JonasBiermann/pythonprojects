C = []
NM = []
t = int(input())
for i in range(t):
    nM = []
    n, m = [int(s) for s in input().split(" ")]
    print(n, m)
    nM.extend([n, m])
    for j in range(t-1):
        c = input().split(" ")
        print(c)
        C.append(c)
    NM.append(nM)
x = 0
print(NM)
bagCon = []
for i in range(t):
    caseList = []
    for j in range(NM[i][0]):
        caseList.append(int(C[i][j]))
    bagCon.append(caseList)
print(bagCon)
amount = 0
for i in range(t):
    for j in range(NM[i][0]):
        amount += bagCon[i][j]
    cPK = amount % NM[i][1]
    print('Case #',i+1,':', cPK)
    amount = 0
