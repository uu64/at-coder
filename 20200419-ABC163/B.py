N, M = map(int, input().split())
A = list(map(int, input().split()))
cost = 0
for a in A:
    cost += a

if N - cost < 0:
    print(-1)
else:
    print(N - cost)
