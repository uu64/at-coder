N, A, B = input().split()
S = input()

rank_a = 0
rank_b = 0
for s in S:
    if s == "a":
        if rank_a + rank_b < A + B:
            print("YES")
            rank_a += 1
        else:
            print("No")
    elif s == "b":
        if rank_a + rank_b < A + B and rank_b < B:
            print("YES")
            rank_b += 1
        else:
            print("No")
    else:
        print("No")
