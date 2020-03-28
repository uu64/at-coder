X = int(input())

q1, mod1 = divmod(X, 500)
q2, mod2 = divmod(mod1, 5)

print(q1*1000 + q2*5)