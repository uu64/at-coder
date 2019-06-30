# -*- coding: utf-8 -*-
import heapq

N, M = map(int, input().split())
MAX = float("inf")

nodes = [[] for i in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    nodes[u].append(v)

S, T = map(int, input().split())
S -= 1
T -= 1

# init
d = [
    [MAX for i in range(N)],
    [MAX for i in range(N)],
    [MAX for i in range(N)],
]
d[0][S] = 0
queue = []
heapq.heappush(queue, [0, 0, S])

while queue:
    p, m, n = heapq.heappop(queue)
    if m == 0 and n == T:
        print(int(p/3))
        quit()
    for to in nodes[n]:
        if d[(m+1) % 3][to] > d[m][n] + 1:
            d[(m+1) % 3][to] = d[m][n] + 1
            heapq.heappush(queue, [
                d[(m+1) % 3][to],
                (m+1) % 3,
                to
            ])

print(-1)
