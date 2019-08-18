# -*- coding: utf-8 -*-

def add(p, x):
    c[p] += x
    for i in E[p]:
        c[i] += x
        for j in E[i]:
            add(j, x)


N, Q = map(int, input().split())
E = [[] for i in range(N+1)]
PX = {}

c = [0 for i in range(N+1)]

for i in range(1, N):
    a, b = map(int, input().split())
    E[a].append(b)

for i in range(1, Q+1):
    p, x = map(int, input().split())
    if p in PX:
        PX[p] += x
    else:
        PX[p] = x


for k in PX.keys():
    add(k, PX[k])

print(' '.join(map(str, c[1:])))