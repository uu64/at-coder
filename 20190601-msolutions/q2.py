import sys


def judge(s):
    win = s.count('o')
    if win >= 8:
        return 'YES'

    if (8 - win) <= (15 - len(s)):
        return 'YES'

    return 'NO'


S = input()

print(judge(S))
