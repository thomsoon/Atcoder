i = int(input())
K = bin(i)[2:]
for k in K:
    if k == '0':
        print('0', end="")
    else:
        print('2', end="")