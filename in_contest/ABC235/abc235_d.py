def one(x):
    return x*a
    
def two(x):
    x = list(str(x))
    result = []
    for i in range(len(x)-1):
        first = x[0]
        x = x[1:]
        x.append(first)
        result.append(int(''.join(x)))
    return result
        
a, N = list(map(int, input().rstrip().split()))
d=[[1]]
i=0
while true:
   o = one(d[i])
   if 
   

