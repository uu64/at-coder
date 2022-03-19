N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

alice = 0
bob = 0

for i in range(N):
    if (i+1) % 2 == 1:
        alice += a[i]
    else:
        bob += a[i]

print(alice - bob)