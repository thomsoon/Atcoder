ans = 0

def dfs(pos, product):
    global ans
    if pos == N:
        #print(product)
        if product == X:
            ans += 1
        return 
    for i in range(1,La[pos][0]+1):
        #print(pos,La[pos][i])
        dfs(pos+1, product*La[pos][i])
        
N, X = list(map(int, input().split()))
La = [list(map(int, input().split())) for i in range(N)]

dfs(0, 1)
print(ans)