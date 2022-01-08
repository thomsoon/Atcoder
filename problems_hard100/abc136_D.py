S = list(input())
result = [0]*len(S)
S.append('E')

r_count = 1
l_count = 0

for i in range(1,len(S)):
    if S[i] == 'R':
        r_count += 1
    elif S[i] == 'L':
        l_count += 1
        if S[i+1] == 'R' or S[i+1] == 'E':
            if (r_count+l_count)%2 == 0:
                result[i-(l_count)] = result[i-(l_count-1)] = int((r_count + l_count)/2)
            else:
                if r_count%2 == 0:
                    result[i-(l_count)] = int((r_count + l_count)/2)
                    result[i-(l_count-1)] = int((r_count + l_count)/2 + 1)
                else :
                    result[i-(l_count)] = int((r_count + l_count)/2+1)
                    result[i-(l_count-1)] = int((r_count + l_count)/2)
            r_count = l_count = 0

for r in result:
    print(r,end=" ")