S = int(input())

C = 1000 - S

coins = [500, 100, 50, 10, 5, 1]

count = 0
for i in coins:
    q, mod = divmod(C, i)
    count += q
    C -= i * q

print(count)