# -*- coding: utf-8 -*-

def conbination(n, r):
    return f[n] // (f[r] * f[n-r])

N, K = map(int, input().split())

f = [1]
for i in range(1, N+1):
    f.append(int(f[i-1]*i))

for i in range(1, K+1):
    if i > N-K+1:
        print(0)
        continue
    c_blue = conbination(K-1, i-1)
    c_red = conbination(N-K+1, i)
    print((c_blue * c_red) % (10**9 + 7))
