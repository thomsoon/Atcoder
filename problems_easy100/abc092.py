N = int(input())
D, X = list(map(int, input().rstrip().split()))
A = [list(map(int, input().rstrip().split())) for i in range(N)]

ans = N
for i in range(N):
    j=1
    while j+A[i][0] <= D:
        j += A[i][0]
        ans += 1


print(ans+X)