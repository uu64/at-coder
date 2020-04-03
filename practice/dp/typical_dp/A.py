import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
p = [0]
p.extend(list(map(int, input().split())))
max_p = sum(p)

memo = [ [ False for i in range(max_p + 1) ] for j in range(N + 1) ]
memo[0][0] = True

def dp(i, j):
    if j < p[i]:
        memo[i][j] = memo[i - 1][j]
    else:
        memo[i][j] = memo[i - 1][j - p[i]] or memo[i - 1][j]


for i in range(1, N + 1):
    for j in range(max_p + 1):
        dp(i, j)

ans = 0
for i in range(max_p + 1):
    if memo[N][i] == True:
        ans += 1
print(ans)
