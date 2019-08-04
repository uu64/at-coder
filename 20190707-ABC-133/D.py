# -*- coding: utf-8 -*-

N = int(input())
A = [
    list(map(int, input().split())),
    [0 for i in range(N)]
]

rain = [0 for i in range(N)]

for i in range(N):
    if i == 0:
        prev = N - 1
    else:
        prev = i - 1

    if A[0][prev] == A[1][prev] or A[0][i] == A[1][i]:
        continue

    tmp  = min(A[0][prev], A[0][i])
    rain[i] = tmp*2
    A[1][prev] = tmp
    A[1][i] = tmp

print(A[1])
print(rain)