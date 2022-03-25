K, N = map(int, input().split())
A = list(map(int, input().split()))

tmp = K - A[N-1]
for i in range(N-1, 0, -1):
    A[i] = A[i] - A[i-1]
A[0] += tmp

A.sort()
print(sum(A[:-1]))