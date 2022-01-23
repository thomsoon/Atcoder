N, M = list(map(int, input().rstrip().split()))
S = list(input().rstrip().split())
T = set(input().rstrip().split())

for v in S:
    if v in T:
        print("Yes")
    else:
        print("No")
