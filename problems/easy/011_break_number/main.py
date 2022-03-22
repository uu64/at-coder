N = int(input())

ans = 0
while 2**ans <= N:
    ans += 1

print(2**(ans - 1))