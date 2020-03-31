import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

field = []
for i in range(N):
    s = input()
    field.append([])
    for j in range(M):
        field[i].append(s[j])

def dfs(i, j):
    if i < 0 or j < 0 or i >= N or j >= M:
        return False

    if field[i][j] == "W":
        field[i][j] = "."
        dfs(i-1, j-1)
        dfs(i-1, j)
        dfs(i-1, j+1)
        dfs(i, j-1)
        dfs(i, j+1)
        dfs(i+1, j-1)
        dfs(i+1, j)
        dfs(i+1, j+1)
        return True
    else:
        return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)
