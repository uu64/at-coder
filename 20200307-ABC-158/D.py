# -*- coding: utf-8 -*-
S = input()
Q = int(input())

reverse = 0
head = []
tail = []
for i in range(Q):
    query = input()
    if len(query) == 1:
        reverse = (reverse + 1) % 2

    else:
        t, F, C = query.split()
        if reverse == 0:
            if F == "1":
                head.append(C)
            else:
                tail.append(C)
        else:
            if F == "1":
                tail.append(C)
            else:
                head.append(C)

if reverse == 0:
    S = ''.join(head[::-1] + list(S) + tail)
else:
    S = ''.join(tail[::-1] + list(S[::-1]) + head)


print(S)
