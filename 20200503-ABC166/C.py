N, M = map(int, input().split())
H = list(map(int, input().split()))

good = [1 for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    if H[A-1] < H[B-1]:
        good[A-1] = 0
    elif H[A-1] > H[B-1]:
        good[B-1] = 0
    else:
        good[A-1] = good[B-1] = 0

count = 0
for g in good:
    if g == 1:
        count += 1

print(count)
