# -*- coding: utf-8 -*-

N, D = map(int, input().split())
X = []

for i in range(N):
    X.append(list(map(int, input().split())))

count = 0
for i in range(N):
    x_i = X[i]
    for j in range(i+1, N):
        x_j = X[j]
        dist = 0
        for d in range(D):
            dist += (x_i[d] - x_j[d])*(x_i[d] - x_j[d])

        dist = dist**0.5
        if dist - int(dist) == 0:
            count += 1

print(count)