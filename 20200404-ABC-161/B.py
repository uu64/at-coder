N, M = map(int, input().split())
A = list(map(int, input().split()))

A_sum = sum(A)
A.sort(reverse=True)

if A[M - 1] >= A_sum * 1 / (4 * M):
    print("Yes")
else:
    print("No")
