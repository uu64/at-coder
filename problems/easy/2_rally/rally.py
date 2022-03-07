N = int(input())
Xs = list(map(int, input().split()))

c = 0
for x in Xs:
    c += x
c = round(c/len(Xs))

ans = 0
for x in Xs:
    ans += (x - c)*(x - c)

print(ans)