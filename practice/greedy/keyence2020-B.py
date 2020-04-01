N = int(input())

arm = []
for i in range(N):
    X, L = map(int, input().split())
    arm.append((X - L, X + L))

arm = sorted(arm, key=lambda x: x[1])

count = 0
i = arm[0][0]
for start, end in arm:
    if start < i:
        continue
    i = end
    count += 1

print(count)
