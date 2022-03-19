N = int(input())
K = int(input())

x = list(map(int, input().split()))

ans = 0
for v in x:
    if K/2 > v:
        ans += v*2
    else:
        ans += (K-v)*2
print(ans)