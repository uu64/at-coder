N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

area = [["." for i in range(S-R+1)] for j in range(Q-P+1)]

min1 = max(1-A, 1-B)
max1 = min(N-A, N-B)
if A > Q or A > S:
    pass
else:
    _A = A - P
    _B = B - R
    for i in range(max1 - min1 + 1):
        if _A + i - 1 < 0 or _B + i - 1 < 0:
            continue
        print("{}, {}".format(_A+i-1, _B+i-1))
        area[_A+i-1][_B+i-1] = "#"

min2 = max(1-A, B-N)
max2 = min(N-A, B-1)
if A < P or A > S:
    pass
else:
    _A = A + P
    _B = B - R
    for i in range(max2 - min2 + 1):
        if _A - i - 1 > N or _B + i - 1 < 0:
            continue
        print("{}, {}".format(_A-i-1, _B+i-1))
        area[_A-i-1][_B+i-1] = "#"

for i in range(Q - P + 1):
    print("".join(area[P + i - 1][R - 1:S]))
