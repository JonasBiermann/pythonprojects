def processCase(case_num):
    (numCandyBags, numKids) = tuple(map(int, input().split()))
    candyCount = list(map(int, input().split()))

    totalCandy = 0
    for i in range(numCandyBags):
        totalCandy += candyCount[i]

    amountRemaining = totalCandy % numKids

    print(f"Case #{case_num}: {amountRemaining}")

numCases = int(input())
for i in range(numCases):
    processCase(i+1)