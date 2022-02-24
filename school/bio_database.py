cat1 = 0
cat2 = 0
cat3 = 0
cat4 = 0
cat5 = 0
cat6 = 0
cat7 = 0
cat8 = 0

for i in range(322):
    a = int(input())
    if (a >= 1982) and (a < 1987):
        cat1 += 1
    if (a >= 1987) and (a <1992):
        cat2 += 1
    if (a >= 1992) and (a <1997):
        cat3 += 1
    if (a >= 1997) and (a <2002):
        cat4 += 1
    if (a >= 2002) and (a < 2007):
        cat5 += 1
    if (a >= 2007) and (a < 2012):
        cat6 += 1
    if (a >= 2012) and (a < 2017):
        cat7 += 1
    if (a >= 2017):
        cat8 += 1

print(cat1)
print(cat2)
print(cat3)
print(cat4)
print(cat5)
print(cat6)
print(cat7)
print(cat8)
