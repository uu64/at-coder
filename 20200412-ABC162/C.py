def gcd(numbers):
    numbers.sort()
    a = numbers[1]
    b = numbers[0]
    ans = b
    while True:
        q, mod = divmod(a, b)
        if mod == 0:
            break
        a = b
        b = mod
        ans = mod
    return ans

K = int(input())
numbers = []

for i in range(K, 0, -1):
    for j in range(i, 0, -1):
        for k in range(j, 0, -1):
            numbers.append([i, j, k])

gcd_sum = 0
for number in numbers:
    dup = len(set(number))
    a, b, c = number
    if dup == 1:
        gcd_sum += gcd([gcd([a, b]), c])
    elif dup == 2:
        gcd_sum += gcd([gcd([a, b]), c]) * 3
    else:
        gcd_sum += gcd([gcd([a, b]), c]) * 6

print(gcd_sum)
