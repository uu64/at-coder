# -*- coding: utf-8 -*-
import math

S = input()
result = [0 for i in range(len(S))]

next_s = 'L'
old_idx = 0
for i in range(len(S)):
    if S[i] == next_s:
        d = i - old_idx
        if next_s == 'L':
            if d % 2 == 0:
                result[i-1] += int(d/2)
                result[i] += int(d/2)
            else:
                result[i-1] += int(d/2) + 1
                result[i] += int(d/2)
            next_s = 'R'
        else:
            if d % 2 == 0:
                result[old_idx-1] += int(d/2)
                result[old_idx] += int(d/2)
            else:
                result[old_idx-1] += int(d/2)
                result[old_idx] += int(d/2) + 1
            next_s = 'L'

        old_idx = i

d = len(S) - old_idx
if d % 2 == 0:
    result[old_idx-1] += int(d/2)
    result[old_idx] += int(d/2)
else:
    result[old_idx-1] += int(d/2)
    result[old_idx] += int(d/2) + 1

for i in result:
    print('{} '.format(i), end='')