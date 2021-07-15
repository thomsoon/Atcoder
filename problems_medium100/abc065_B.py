
import io
import sys
_INPUT = """\
5
3
3
4
2
4
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

num = a[0]
if num == 2:
    print("1")
else:
    count = 1
    for i in range(N):
        num = a[num-1]
        count += 1
        if num == 2:
            break
    
    if num == 2:
        print(count)
    else:
        print("-1")