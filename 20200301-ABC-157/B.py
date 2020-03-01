# -*- coding: utf-8 -*-

answers = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

A = []
A.extend(list(map(int, input().split())))
A.extend(list(map(int, input().split())))
A.extend(list(map(int, input().split())))

N = int(input())

b = []
for i in range(N):
    b.append(int(input()))

hole = []
for i in b:
    if i in A:
        hole.append(A.index(i))
    else:
        continue

for answer in answers:
    i, j, k = answer
    if i in hole and j in hole and k in hole:
        print("Yes")
        exit(0)
print("No")
