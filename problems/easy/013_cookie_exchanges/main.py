A, B, C = map(int, input().split())

c = 0
while True:
    if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
        break
    if A == B and A == C:
        c = -1
        break
    tmpA = A
    tmpB = B
    tmpC = C
    A = int(tmpB/2) + int(tmpC/2)
    B = int(tmpA/2) + int(tmpC/2)
    C = int(tmpB/2) + int(tmpA/2)
    c += 1
print(c)