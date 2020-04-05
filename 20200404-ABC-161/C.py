N, K = map(int, input().split())

q, mod = divmod(N, K)

print(min(mod, abs(mod - K)))
