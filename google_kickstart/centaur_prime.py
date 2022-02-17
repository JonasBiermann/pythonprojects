def processCase(caseNum):
    c = [['b'], ['c'], ['d'], ['f'], ['g'], ['h'], ['j'], ['k'], ['l'], ['m'], ['n'], ['p'], ['q'], ['r'], ['s'], ['t'], ['v'], ['w'], ['x'], ['z']]
    v = [['a'], ['e'], ['i'], ['o'], ['u']]
    kingdomName = input().split()
    if kingdomName[0][-1] != 'y':
        for i in range(len(c)):
            if kingdomName[0][-1] == c[i][0]:
                print(f'Case #{caseNum}: {kingdomName[0]} is ruled by Bob.')
    if kingdomName[0][-1] != 'y':
        for j in range(len(v)):
            if kingdomName[0][-1] == v[j][0]:
                print(f'Case #{caseNum}: {kingdomName[0]} is ruled by Alice.')
    if kingdomName[0][-1] == 'y': 
        print(f'Case #{caseNum}: {kingdomName[0]} is ruled by nobody.')

caseNum = int(input())
for i in range(caseNum):
    processCase(i+1)