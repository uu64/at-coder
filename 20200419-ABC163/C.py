N = int(input())
A = list(map(int, input().split()))

A.sort()
for i in range(1, A[0]):
    print(0)

idx = 0
for shain in range(A[0], N+1):
    num = 0
    while True:
        if idx >= N - 1:
            print(num)
            num = 0
            break
        if shain != A[idx]:
            print(num)
            num = 0
            shain += 1
            break
        else:
            num += 1
            idx += 1

