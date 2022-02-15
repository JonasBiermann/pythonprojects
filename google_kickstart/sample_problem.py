textFile = """2
7 3
1 2 3 4 5 6 7
5 10
7 7 7 7 7
"""
lines = []
for line in textFile.splitlines():
    lines.append(line.split())
cases = int(lines[0][0])
nM = []
C = []
x = 1
for i in range(cases):
    caseList = []
    for j in range(cases):
        caseList.append((int(lines[x][j])))
    nM.append(caseList)
    x = 3
i = 0
j = 0
x = 2
for i in range(cases):
    caseList = []
    for j in range(nM[i][0]):
        caseList.append(int(lines[x][j]))
    C.append(caseList)
    x = 4
i = 0
j = 0
amount = 0
for i in range(cases):
    for j in range(nM[i][0]):
        amount += C[i][j]
    cPK = amount % nM[i][1]
    print('Case #', i+1,': ', cPK)
    amount = 0