# coding: utf-8
N = int(input())
H = list(map(int, input().rstrip().split()))
now = H[0]
for i in range(1,N):
    now
    if H[i] > now:
        now = H[i]
    else:
        break
print(now)