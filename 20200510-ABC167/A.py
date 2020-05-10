S = input()
T = input()

if len(S) >= 1 and len(S) <= 10 and len(S)+1 == len(T) and S == T[0:-1] :
    print("Yes")
else:
    print("No")
