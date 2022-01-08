import math

N = int(input())
XY = [list(map(int, input().split())) for i in range(int(N))]


max_len = 0
for i in range(len(XY)):
    for j in range(i+1,len(XY)):
        x = XY[j][0] - XY[i][0]
        y = XY[j][1] - XY[i][1]
        l = math.sqrt(x*x + y*y)
        if max_len < l:
            max_len = l
            
print(max_len)