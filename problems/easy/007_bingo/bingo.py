import sys

sheet = [False for i in range(9)]
A = []
for i in range(3):
    A.extend(list(map(int, input().split())))

N = int(input())
for i in range(N):
    b = int(input())
    if b in A:
        sheet[A.index(b)] = True

pat = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

for p in pat:
    if sheet[p[0]] and sheet[p[1]] and sheet[p[2]]:
        print("Yes")
        sys.exit(0)

print("No")