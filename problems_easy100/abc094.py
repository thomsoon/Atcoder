N,M,X = list(map(int,input().rstrip().split()))
A = list(map(int,input().rstrip().split()))

cost=0

cost_p=0
cost_m=0
for i in range(X+1, N+1):
    if i in A:
        cost_p += 1
for i in range(X-1, -1, -1):
    if i in A:
        cost_m += 1
cost = min(cost_p,cost_m)
print(cost)