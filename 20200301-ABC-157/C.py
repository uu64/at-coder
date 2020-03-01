# -*- coding: utf-8 -*-

N, M = map(int, input().split())
result = [-1] * N

for i in range(1, M + 1):
    s, c = map(int, input().split())
    if result[s - 1] == -1:
        result[s - 1] = c
    elif result[s - 1] == c:
        continue
    else:
        print(-1)
        exit(0)

if N != 1 and result[0] == 0:
    print(-1)
    exit(0)

if N == 1 and result[0] == -1:
    print(0)
    exit(0)

if N != 1 and result[0] == -1:
    result[0] = 1

for i in range(len(result)):
    if result[i] == -1:
        print(0, end="")
    else:
        print(result[i], end="")
print()
