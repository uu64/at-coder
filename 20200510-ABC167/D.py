N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
history = [1]
index = -1

while count <= K:
    current = history[-1]
    _next = A[current - 1]
    if _next in history:
        index = history.index(_next)
        break
    else:
        history.append(_next)
    count += 1

if index == -1:
    print(history[-1])
else:
    loop = history[index:]
    q, mod = divmod(K - count - (len(history) - index), len(loop))
    print(loop[mod - 1])
