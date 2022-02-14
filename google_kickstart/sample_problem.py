import linecache


textFile = """2
7 3
1 2 3 4 5 6 7
5 10
7 7 7 7 7
"""
lines = []
for line in textFile.splitlines():
    print(line)
    lines.append(line.split())

print(lines)
cases = int(lines[0][0])
nM = []
C = []
x = 1
for i in range(cases):
    for j in range(cases):
        nM.append((int(lines[x][j])))
    x = 3

print(nM)
# print(nM[0])
# for j in range(int(nM[0])):
#     C.append(int(lines[2][j]))

# print(nM, C)

# i = 0
# j = 0
# print(type(nM))
# print(type(C[0]))
# amount = 0

# for i in range(cases):
#     for j in range(nM[i]):
#         amount += C[j]     
#     cPK = amount % nM[1] 
#     print('Case #', i+1,': ', cPK)
#     amount = 0

