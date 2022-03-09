from re import I


N = int(input())

v, m = divmod(N*100, 108)

if m == 0:
    print(v)
else:
    if (v+1)*1.08 < N+1:
        print(v+1)
    else:
        print(":(")