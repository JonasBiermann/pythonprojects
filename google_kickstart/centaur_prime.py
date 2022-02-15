input = """3
Mollaristan
Auritania
Zizily
"""

sampleInput = []
sampleInput.append(input.split())
cases = int(sampleInput[0][0])

letters = []
x = 1
for i in range(cases):
    letters.append(sampleInput[0][x][-1])
    x += 1

for i in range(len(letters)):
    if letters[i] == 'n':
        print('Case #', i+1,': ', sampleInput[0][i+1], 'is ruled by Bob.')
    if letters[i] == 'a':
        print('Case #', i+1,': ', sampleInput[0][i+1], 'is ruled by Alice.')
    if letters[i] == 'y':
        print('Case #', i+1,': ', sampleInput[0][i+1], 'is ruled by nobody.')