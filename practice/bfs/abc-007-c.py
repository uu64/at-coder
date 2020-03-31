import sys
sys.setrecursionlimit(10 ** 6)

from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

field = []

for i in range(R):
    s = input()
    field.append([])
    for j in range(C):
        field[i].append(s[j])


def canMove(i, j):
    if i < 0 or j < 0:
        return False
    if i >= R or j >= C:
        return False
    if field[i][j] != ".":
        return False
    return True

d = deque()
d.append((sy - 1, sx - 1))
field[sy - 1][sx - 1] = 0
while len(d) > 0:
    i, j = d.popleft()
    if i == gy - 1 and j == gx - 1:
        print(field[i][j])
        break

    if canMove(i - 1, j):
        d.append((i - 1, j))
        field[i - 1][j] = field[i][j] + 1
    if canMove(i, j - 1):
        d.append((i, j - 1))
        field[i][j - 1] = field[i][j] + 1
    if canMove(i, j + 1):
        d.append((i, j + 1))
        field[i][j + 1] = field[i][j] + 1
    if canMove(i + 1, j):
        d.append((i + 1, j))
        field[i + 1][j] = field[i][j] + 1
