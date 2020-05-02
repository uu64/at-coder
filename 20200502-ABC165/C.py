import sys
sys.setrecursionlimit(10 ** 6)

N, M, Q = map(int, input().split())
A = []
for i in range(Q):
    A.append(list(map(int, input().split())))

numbers = []
count = 0
def dfs(num_list):
    last = num_list[-1]
    if len(num_list) == N:
        numbers.append(num_list)
    else:
        for i in range(last, M+1):
            tmp = num_list[:]
            tmp.append(i)
            dfs(tmp)

for i in range(1, M+1):
    dfs([i])

_max = 0
for number in numbers:
    _sum = 0
    for i in range(Q):
        if number[A[i][1] - 1] - number[A[i][0] - 1] == A[i][2]:
            _sum += A[i][3]
    if _max < _sum:
        _max = _sum
print(_max)
