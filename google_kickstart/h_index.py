def score(x: int, A: list):
    total = sum(A[x:])
    return total

def calculate_hindex(N: int, citations: list):
    A = [0] * (N+1)
    ans = []
    hindex = 0
    for i in range(N):
        A[N if citations[i]>N else citations[i]]+=1
        j = i+1
        while j and j >hindex:
            if (score(j, A)>= j):
                hindex = j
                break
            j -= 1
        ans.append(hindex)
    return ans

caseNum = int(input())
for i in range(caseNum):
    N = int(input())
    A = list(map(int, input().split()))
    print('Case #', i+1, calculate_hindex(N, A))