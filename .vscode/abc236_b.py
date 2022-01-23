N = int(input())
A = list(map(int, input().rstrip().split()))

result = [0]*N
for v in A:
    result[v-1] += 1
    
print(result.index(3)+1)