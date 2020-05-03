N, K = map(int, input().split())

sunuke = [0 for i in range(N+1)]

for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for _a in A:
        sunuke[_a] = 1

count = 0
for i in range(1, N+1):
    if sunuke[i] == 0:
        count += 1

print(count)
