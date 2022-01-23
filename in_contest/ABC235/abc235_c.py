N,Q = list(map(int, input().rstrip().split()))
A = list(map(int, input().rstrip().split()))
XK=[list(map(int, input().split())) for i in range(int(Q))]

d={}
for i,v in enumerate(A):
    if v in d:
        d[v].append(i)
    else:
        d[v]=[i]
        
for v in XK:
    x, k = v
    if x not in d:
        print(-1)
        continue
    if k-1 < len(d[x]):
        print(d[x][k-1]+1)
    else:
        print(-1)