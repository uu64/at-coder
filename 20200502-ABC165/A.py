K = int(input())
A, B = map(int, input().split())

q1, mod1 = divmod(A, K)
q2, mod2 = divmod(B, K)

if mod1 == 0:
    print("OK")
elif mod2 == 0:
    print("OK")
elif A + K - mod1 <= B:
    print("OK")
else:
    print("NG")
