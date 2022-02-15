input = """2
3
5 1 2
6
1 3 3 2 2 15
"""
sampleInput = []
for line in input.splitlines():
    sampleInput.append(line.split())

print(sampleInput)

cases = int(sampleInput[0][0])

paperCount = []
x = 1
for i in range(cases):
    paperCount.append(int(sampleInput[x][0]))
    x = 3

citationCount = []
x = 2
for i in range(cases):
    citPap = []
    for j in range(paperCount[i]):
        citPap.append(int(sampleInput[x][j]))
    citationCount.append(citPap)
    x = 4

print(citationCount)

h_index = []

for i in range(cases):
    h = 0
    citations = 1
    sample_h = []
    
    for j in range(paperCount[i]):
        
        if citationCount[i][j] >= citations*(j+1):
            h += 1
        sample_h.append(h)
    h_index.append(sample_h)

print(h_index)