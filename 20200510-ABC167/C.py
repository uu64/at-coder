import sys
sys.setrecursionlimit(10 ** 6)

N, M, X = map(int, input().split())
C = []
A = []

for i in range(N):
    S = list(map(int, input().split()))
    C.append(S[0])
    A.append(S[1:])

patterns = []

def dfs(buyable, pattern, idx):
    copy = pattern[:]
    if len(copy) == buyable:
        patterns.append(copy)
    elif idx == N:
        return
    else:
        dfs(buyable, copy, idx+1)
        copy.append(idx)
        dfs(buyable, copy, idx+1)

achived = False
_min = sum(C)
for i in range(1, N+1):
    patterns = []
    dfs(i, [], 0)

    for pattern in patterns:
        total = 0
        tmp = [0 for i in range(M)]
        for j in pattern:
            total += C[j]
            for k in range(M):
                tmp[k] += A[j][k]

        if min(tmp) >= X and _min >= total:
            _min = total
            achived = True

if achived:
    print(_min)
else:
    print(-1)
