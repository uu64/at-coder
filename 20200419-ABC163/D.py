N, K = map(int, input().split())
number = [ i for i in range(0, N + 1)]


left = number[K - 1]
right = number[-K]
s_min = sum(number[0:K])
s_max = sum(number[-K:])
count = s_max - s_min + 1
for i in range(K + 1, N + 2):
    left += 1
    right -= 1
    s_min += left
    s_max += right
    count += s_max - s_min + 1
print(count % 1000000007)
